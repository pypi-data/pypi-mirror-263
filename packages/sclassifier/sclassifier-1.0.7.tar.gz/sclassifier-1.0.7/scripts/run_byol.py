#!/usr/bin/env python

from __future__ import print_function

##################################################
###    SET SEED FOR REPRODUCIBILITY (DEBUG)
##################################################
#from numpy.random import seed
#seed(1)
#import tensorflow
#tensorflow.random.set_seed(2)

##################################################
###          MODULE IMPORT
##################################################
## STANDARD MODULES
import os
import sys
import subprocess
import string
import time
import signal
from threading import Thread
import datetime
import numpy as np
import random
import math
import logging
import json

## COMMAND-LINE ARG MODULES
import getopt
import argparse
import collections

## MODULES
from sclassifier import __version__, __date__
from sclassifier import logger
from sclassifier.feature_extractor_byol import FeatExtractorByol
from sclassifier.data_generator import DataGenerator
from sclassifier.preprocessing import DataPreprocessor
from sclassifier.preprocessing import BkgSubtractor, SigmaClipper, SigmaClipShifter, Scaler, LogStretcher, Augmenter
from sclassifier.preprocessing import Resizer, MinMaxNormalizer, AbsMinMaxNormalizer, MaxScaler, AbsMaxScaler, ChanMaxScaler
from sclassifier.preprocessing import Shifter, Standardizer, ChanDivider, MaskShrinker, BorderMasker
from sclassifier.preprocessing import ChanResizer, ZScaleTransformer, Chan3Trasformer

#### GET SCRIPT ARGS ####
def str2bool(v):
	if v.lower() in ('yes', 'true', 't', 'y', '1'):
		return True
	elif v.lower() in ('no', 'false', 'f', 'n', '0'):
		return False
	else:
		raise argparse.ArgumentTypeError('Boolean value expected.')

###########################
##     ARGS
###########################
def get_args():
	"""This function parses and return arguments passed in"""
	parser = argparse.ArgumentParser(description="Parse args.")

	# - Input options
	parser.add_argument('-datalist','--datalist', dest='datalist', required=True, type=str, help='Input data json filelist') 
	parser.add_argument('-datalist_cv','--datalist_cv', dest='datalist_cv', required=False, default="", type=str, help='Input data json filelist for validation') 
	
	# - Data pre-processing options
	parser.add_argument('--no-resize', dest='resize', action='store_false',help='Resize images')	
	parser.set_defaults(resize=True)
	parser.add_argument('-resize_size', '--resize_size', dest='resize_size', required=False, type=int, default=64, action='store',help='Image resize in pixels (default=64)')	
	parser.add_argument('--downscale_with_antialiasing', dest='downscale_with_antialiasing', action='store_true', help='Use anti-aliasing when downsampling the image (default=no)')	
	parser.set_defaults(downscale_with_antialiasing=False)
	parser.add_argument('--upscale', dest='upscale', action='store_true', help='Upscale images to resize size when source size is smaller (default=no)')	
	parser.set_defaults(upscale=False)
	parser.add_argument('--set_pad_val_to_min', dest='set_pad_val_to_min', action='store_true', help='Set masked value in resized image to min, otherwise leave to masked values (default=no)')	
	parser.set_defaults(set_pad_val_to_min=False)

	parser.add_argument('-augmenter', '--augmenter', dest='augmenter', required=False, type=str, default='byol', action='store',help='Predefined augmenter to be used (default=byol)')

	parser.add_argument('--normalize_minmax', dest='normalize_minmax', action='store_true',help='Normalize each channel in range [0,1]')	
	parser.set_defaults(normalize_minmax=False)
	parser.add_argument('--normalize_absminmax', dest='normalize_absminmax', action='store_true',help='Normalize each channel in range using absolute min/max computed over all channels [0,1]')	
	parser.set_defaults(normalize_absminmax=False)

	parser.add_argument('--scale_to_abs_max', dest='scale_to_abs_max', action='store_true',help='Scale to global max across all channels')	
	parser.set_defaults(scale_to_abs_max=False)
	parser.add_argument('--scale_to_max', dest='scale_to_max', action='store_true',help='Scale to max not to min-max range')	
	parser.set_defaults(scale_to_max=False)
	parser.add_argument('--scale_to_selch_max', dest='scale_to_selch_max', action='store_true',help='Scale to selected channel max not to min-max range')	
	parser.set_defaults(scale_to_selch_max=False)
	parser.add_argument('--use_box_mask_in_chan_max_scaler', dest='use_box_mask_in_chan_max_scaler', action='store_true',help='Find chan max for scaling inside box mask')	
	parser.set_defaults(use_box_mask_in_chan_max_scaler=False)	
	parser.add_argument('-chan_max_scaler_box_mask_fract', '--chan_max_scaler_box_mask_fract', dest='chan_max_scaler_box_mask_fract', required=False, type=float, default=0.5, action='store',help='Size of mask box dimensions with respect to image size used in chan max scaler (default=0.5)')
	
	parser.add_argument('--log_transform', dest='log_transform', action='store_true',help='Apply log transform to images')	
	parser.set_defaults(log_transform=False)
	parser.add_argument('-log_transform_chid', '--log_transform_chid', dest='log_transform_chid', required=False, type=int, default=-1, action='store',help='Channel id to be excluded from log-transformed. -1=transform all (default=-1)')
	parser.add_argument('--log_transform_minmaxnorm', dest='log_transform_minmaxnorm', action='store_true',help='Apply min/max normalization after log transform to images')	
	parser.set_defaults(log_transform_minmaxnorm=False)
	parser.add_argument('-log_transform_normmin', '--log_transform_normmin', dest='log_transform_normmin', required=False, type=float, default=-6, action='store',help='Min data normalization value to be applied if log_transform_minmaxnorm is enabled (default=-6)')
	parser.add_argument('-log_transform_normmax', '--log_transform_normmax', dest='log_transform_normmax', required=False, type=float, default=6, action='store',help='Max data normalization value to be applied if log_transform_minmaxnorm is enabled (default=6)')
	parser.add_argument('--log_transform_clipneg', dest='log_transform_clipneg', action='store_true',help='Clip negative values to 0 after min/max norm')	
	parser.set_defaults(log_transform_clipneg=False)

	parser.add_argument('--scale', dest='scale', action='store_true',help='Apply scale factors to images')	
	parser.set_defaults(scale=False)
	parser.add_argument('-scale_factors', '--scale_factors', dest='scale_factors', required=False, type=str, default='', action='store',help='Image scale factors separated by commas (default=empty)')

	parser.add_argument('--standardize', dest='standardize', action='store_true',help='Apply standardization to images')	
	parser.set_defaults(standardize=False)
	parser.add_argument('--meanshift', dest='meanshift', action='store_true',help='Apply mean shift to images')	
	parser.set_defaults(meanshift=False)
	parser.add_argument('-img_means', '--img_means', dest='img_means', required=False, type=str, default='', action='store',help='Image means (separated by commas) to be used in standardization (default=empty)')
	parser.add_argument('-img_sigmas', '--img_sigmas', dest='img_sigmas', required=False, type=str, default='', action='store',help='Image sigmas (separated by commas) to be used in standardization (default=empty)')

	parser.add_argument('--erode', dest='erode', action='store_true',help='Apply erosion to image sourve mask')	
	parser.set_defaults(erode=False)	
	parser.add_argument('-erode_kernel', '--erode_kernel', dest='erode_kernel', required=False, type=int, default=5, action='store',help='Erosion kernel size in pixels (default=5)')	

	parser.add_argument('--subtract_bkg', dest='subtract_bkg', action='store_true',help='Subtract bkg from ref channel image')	
	parser.set_defaults(subtract_bkg=False)
	parser.add_argument('-sigma_bkg', '--sigma_bkg', dest='sigma_bkg', required=False, type=float, default=3, action='store',help='Sigma clip to be used in bkg calculation (default=3)')
	parser.add_argument('--use_box_mask_in_bkg', dest='use_box_mask_in_bkg', action='store_true',help='Compute bkg value in borders left from box mask')	
	parser.set_defaults(use_box_mask_in_bkg=False)	
	parser.add_argument('-bkg_box_mask_fract', '--bkg_box_mask_fract', dest='bkg_box_mask_fract', required=False, type=float, default=0.7, action='store',help='Size of mask box dimensions with respect to image size used in bkg calculation (default=0.7)')
	parser.add_argument('-bkg_chid', '--bkg_chid', dest='bkg_chid', required=False, type=int, default=-1, action='store',help='Channel to subtract background (-1=all) (default=-1)')

	parser.add_argument('--clip_shift_data', dest='clip_shift_data', action='store_true',help='Do sigma clipp shifting')	
	parser.set_defaults(clip_shift_data=False)
	parser.add_argument('-sigma_clip', '--sigma_clip', dest='sigma_clip', required=False, type=float, default=1, action='store',help='Sigma threshold to be used for clip & shifting pixels (default=1)')
	parser.add_argument('--clip_data', dest='clip_data', action='store_true',help='Do sigma clipping')	
	parser.set_defaults(clip_data=False)
	parser.add_argument('-sigma_clip_low', '--sigma_clip_low', dest='sigma_clip_low', required=False, type=float, default=10, action='store',help='Lower sigma threshold to be used for clipping pixels below (mean-sigma_low*stddev) (default=10)')
	parser.add_argument('-sigma_clip_up', '--sigma_clip_up', dest='sigma_clip_up', required=False, type=float, default=10, action='store',help='Upper sigma threshold to be used for clipping pixels above (mean+sigma_up*stddev) (default=10)')	
	parser.add_argument('-clip_chid', '--clip_chid', dest='clip_chid', required=False, type=int, default=-1, action='store',help='Channel to clip data (-1=all) (default=-1)')

	parser.add_argument('--mask_borders', dest='mask_borders', action='store_true',help='Mask image borders by desired width/height fraction')
	parser.set_defaults(mask_borders=False)
	parser.add_argument('-mask_border_fract', '--mask_border_fract', dest='mask_border_fract', required=False, type=float, default=0.7, action='store',help='Size of non-masked box dimensions with respect to image size (default=0.7)')

	parser.add_argument('--resize_chans', dest='resize_chans', action='store_true',help='Resize channels to desired number specified in nchan_resize')	
	parser.set_defaults(resize_chans=False)
	parser.add_argument('-nchan_resize', '--nchan_resize', dest='nchan_resize', required=False, type=int, default=3, action='store',help='Desired number of channels for resizing (default=3)')

	parser.add_argument('--zscale_stretch', dest='zscale_stretch', action='store_true',help='Do zscale transform')	
	parser.set_defaults(zscale_stretch=False)
	parser.add_argument('--zscale_contrasts', dest='zscale_contrasts', required=False, type=str, default='0.25,0.25,0.25',help='zscale contrasts applied to all channels') 
	
	parser.add_argument('--chan3_preproc', dest='chan3_preproc', action='store_true',help='Use the 3 channel pre-processor')	
	parser.set_defaults(chan3_preproc=False)
	parser.add_argument('-sigma_clip_baseline', '--sigma_clip_baseline', dest='sigma_clip_baseline', required=False, type=float, default=0, action='store',help='Lower sigma threshold to be used for clipping pixels below (mean-sigma_low*stddev) in first channel of 3-channel preprocessing (default=0)')
	parser.add_argument('-nchannels', '--nchannels', dest='nchannels', required=False, type=int, default=-1, action='store',help='Number of channels (if -1=take from data generator). If you modify channels in preprocessing you must set this (default=-1)')

	# - Network training options
	parser.add_argument('-nepochs', '--nepochs', dest='nepochs', required=False, type=int, default=100, action='store',help='Number of epochs used in network training (default=100)')	
	parser.add_argument('-optimizer', '--optimizer', dest='optimizer', required=False, type=str, default='rmsprop', action='store',help='Optimizer used (default=rmsprop)')
	parser.add_argument('-learning_rate', '--learning_rate', dest='learning_rate', required=False, type=float, default=None, action='store',help='Learning rate. If None, use default for the selected optimizer (default=None)')
	parser.add_argument('-batch_size', '--batch_size', dest='batch_size', required=False, type=int, default=32, action='store',help='Batch size used in training (default=32)')
	parser.add_argument('-weight_seed', '--weight_seed', dest='weight_seed', required=False, type=int, default=None, action='store',help='Weight seed to set reproducible training (default=None)')
	parser.add_argument('--reproducible', dest='reproducible', action='store_true',help='Fix seed and make model reproducible from run to run')	
	parser.set_defaults(reproducible=False)
	parser.add_argument('-validation_steps', '--validation_steps', dest='validation_steps', required=False, type=int, default=10, action='store',help='Number of validation steps used in each epoch (default=10)')

	parser.add_argument('--no-multiprocessing', dest='multiprocessing', action='store_false',help='Disable multiprocessing in TF fit method (default=enabled)')	
	parser.set_defaults(multiprocessing=True)

	parser.add_argument('--load_cv_data_in_batches', dest='load_cv_data_in_batches', action='store_true',help='Load validation data in batches using train batch size (default=load all data in a single step)')	
	parser.set_defaults(load_cv_data_in_batches=False)

	parser.add_argument('--balance_classes_in_batch', dest='balance_classes_in_batch', action='store_true',help='Balance classes in batch generation')	
	parser.set_defaults(balance_classes_in_batch=False)
	parser.add_argument('--class_probs', dest='class_probs', required=False, type=str, default='{"PN":1,"HII":1,"PULSAR":1,"YSO":1,"STAR":1,"GALAXY":1,"QSO":1}', help='Class weights used in batch rebalance') 
	

	# - Network architecture options
	parser.add_argument('-weightfile_encoder', '--weightfile_encoder', dest='weightfile_encoder', required=False, type=str, default="", action='store',help='Encoder weight file (hd5) to be loaded (default=no)')	
	parser.add_argument('-modelfile_encoder', '--modelfile_encoder', dest='modelfile_encoder', required=False, type=str, default="", action='store',help='Encoder model architecture file (json) to be loaded (default=no)')
	parser.add_argument('-weightfile_projector', '--weightfile_projector', dest='weightfile_projector', required=False, type=str, default="", action='store',help='Projector weight file (hd5) to be loaded (default=no)')	
	parser.add_argument('-modelfile_projector', '--modelfile_projector', dest='modelfile_projector', required=False, type=str, default="", action='store',help='Projector model architecture file (json) to be loaded (default=no)')
	parser.add_argument('-weightfile_predictor', '--weightfile_predictor', dest='weightfile_predictor', required=False, type=str, default="", action='store',help='Predictor weight file (hd5) to be loaded (default=no)')	
	parser.add_argument('-modelfile_predictor', '--modelfile_predictor', dest='modelfile_predictor', required=False, type=str, default="", action='store',help='Predictor model architecture file (json) to be loaded (default=no)')
	parser.add_argument('-latentdim', '--latentdim', dest='latentdim', required=False, type=int, default=2, action='store',help='Dimension of latent vector (default=2)')	
	parser.add_argument('--add_maxpooling_layer', dest='add_maxpooling_layer', action='store_true',help='Add max pooling layer after conv layers ')	
	parser.set_defaults(add_maxpooling_layer=False)	
	parser.add_argument('--add_batchnorm_layer', dest='add_batchnorm_layer', action='store_true',help='Add batch normalization layer after conv layers ')	
	parser.set_defaults(add_batchnorm_layer=False)	
	parser.add_argument('--add_leakyrelu', dest='add_leakyrelu', action='store_true',help='Add LeakyRELU after batch norm layers ')	
	parser.set_defaults(add_leakyrelu=False)
	parser.add_argument('--add_dense_layer', dest='add_dense_layer', action='store_true',help='Add dense layers in encoder after flattening layers ')	
	parser.set_defaults(add_dense_layer=False)
	parser.add_argument('--add_dropout_layer', dest='add_dropout_layer', action='store_true',help='Add dropout layers before dense layers')	
	parser.set_defaults(add_dropout_layer=False)
	parser.add_argument('-dropout_rate', '--dropout_rate', dest='dropout_rate', required=False, type=float, default=0.5, action='store',help='Dropout rate (default=0.5)')

	parser.add_argument('--add_conv_dropout_layer', dest='add_conv_dropout_layer', action='store_true',help='Add dropout layers after conv max pool layers')	
	parser.set_defaults(add_conv_dropout_layer=False)
	parser.add_argument('-conv_dropout_rate', '--conv_dropout_rate', dest='conv_dropout_rate', required=False, type=float, default=0.2, action='store',help='Dropout rate after conv layers (default=0.2)')


	parser.add_argument('-nfilters_cnn', '--nfilters_cnn', dest='nfilters_cnn', required=False, type=str, default='32,64,128', action='store',help='Number of convolution filters per each layer')
	parser.add_argument('-kernsizes_cnn', '--kernsizes_cnn', dest='kernsizes_cnn', required=False, type=str, default='3,5,7', action='store',help='Convolution filter kernel sizes per each layer')
	parser.add_argument('-strides_cnn', '--strides_cnn', dest='strides_cnn', required=False, type=str, default='2,2,2', action='store',help='Convolution strides per each layer')
	
	parser.add_argument('-dense_layer_sizes', '--dense_layer_sizes', dest='dense_layer_sizes', required=False, type=str, default='16', action='store',help='Dense layer sizes used (default=16)')
	parser.add_argument('-dense_layer_activation', '--dense_layer_activation', dest='dense_layer_activation', required=False, type=str, default='relu', action='store',help='Dense layer activation used {relu,softmax} (default=relu)')

	parser.add_argument('--use_predefined_arch', dest='use_predefined_arch', action='store_true',help='Use pre-defined conv architecture and not a custom ones (default=false)')	
	parser.set_defaults(use_predefined_arch=False)
	parser.add_argument('-predefined_arch', '--predefined_arch', dest='predefined_arch', required=False, type=str, default='resnet50', action='store',help='Predefined architecture to be used {resnet18, resnet34, resnet50, resnet101}')

	# - Run options
	parser.add_argument('--predict', dest='predict', action='store_true',help='Predict model on input data (default=false)')	
	parser.set_defaults(predict=False)

	# - Save options
	parser.add_argument('--no_save_embeddings', dest='no_save_embeddings', action='store_true',help='Do not save embeddings (default=true)')	
	parser.set_defaults(no_save_embeddings=False)

	parser.add_argument('--save_tb_embeddings', dest='save_tb_embeddings', action='store_true',help='Save embeddings & images in Tensorboard format (default=false)')	
	parser.set_defaults(save_tb_embeddings=False)

	parser.add_argument('-nembeddings_save', '--nembeddings_save', dest='nembeddings_save', required=False, type=int, default=1000, action='store', help='Number of images/embeddings to be saved (default=1000)')

	parser.add_argument('-img_embedding_scale', '--img_embedding_scale', dest='img_embedding_scale', required=False, type=float, default=1.0, action='store', help='If <1 rescale input image before creating preview sprite (default=1.0)')
	
	parser.add_argument('--shuffle_embeddings', dest='shuffle_embeddings', action='store_true',help='Shuffle embeddings to be saved (default=false)')	
	parser.set_defaults(shuffle_embeddings=False)
	
	args = parser.parse_args()	

	return args



##############
##   MAIN   ##
##############
def main():
	"""Main function"""

	
	#===========================
	#==   PARSE ARGS
	#===========================
	logger.info("Get script args ...")
	try:
		args= get_args()
	except Exception as ex:
		logger.error("Failed to get and parse options (err=%s)",str(ex))
		return 1

	# - Input filelist
	datalist= args.datalist
	datalist_cv= args.datalist_cv
	
	# - Data process options	
	resize= args.resize
	resize_size= args.resize_size
	downscale_with_antialiasing= args.downscale_with_antialiasing
	upscale= args.upscale
	set_pad_val_to_min= args.set_pad_val_to_min
	augmenter= args.augmenter
	scale= args.scale
	scale_factors= []
	if args.scale_factors!="":
		scale_factors= [float(x.strip()) for x in args.scale_factors.split(',')]

	normalize_minmax= args.normalize_minmax
	normalize_absminmax= args.normalize_absminmax
	scale_to_abs_max= args.scale_to_abs_max
	scale_to_max= args.scale_to_max
	scale_to_selch_max= args.scale_to_selch_max
	use_box_mask_in_chan_max_scaler= args.use_box_mask_in_chan_max_scaler
	chan_max_scaler_box_mask_fract= args.chan_max_scaler_box_mask_fract
	log_transform= args.log_transform
	log_transform_chid= args.log_transform_chid
	log_transform_minmaxnorm= args.log_transform_minmaxnorm
	log_transform_normmin= args.log_transform_normmin
	log_transform_normmax= args.log_transform_normmax
	log_transform_clipneg= args.log_transform_clipneg
	standardize= args.standardize
	meanshift= args.meanshift
	img_means= []
	img_sigmas= []
	if args.img_means!="":
		img_means= [float(x.strip()) for x in args.img_means.split(',')]
	if args.img_sigmas!="":
		img_sigmas= [float(x.strip()) for x in args.img_sigmas.split(',')]

	erode= args.erode	
	erode_kernel= args.erode_kernel

	subtract_bkg= args.subtract_bkg
	sigma_bkg= args.sigma_bkg
	use_box_mask_in_bkg= args.use_box_mask_in_bkg
	bkg_box_mask_fract= args.bkg_box_mask_fract
	bkg_chid= args.bkg_chid
	clip_shift_data= args.clip_shift_data
	clip_data= args.clip_data
	sigma_clip= args.sigma_clip
	sigma_clip_low= args.sigma_clip_low
	sigma_clip_up= args.sigma_clip_up
	clip_chid= args.clip_chid
	mask_borders= args.mask_borders
	mask_border_fract= args.mask_border_fract

	resize_chans= args.resize_chans
	nchan_resize= args.nchan_resize

	zscale_stretch= args.zscale_stretch
	zscale_contrasts= [float(x) for x in args.zscale_contrasts.split(',')]

	chan3_preproc= args.chan3_preproc
	sigma_clip_baseline= args.sigma_clip_baseline
	nchannels= args.nchannels

	# - Model architecture
	modelfile_encoder= args.modelfile_encoder
	weightfile_encoder= args.weightfile_encoder
	modelfile_projector= args.modelfile_projector
	weightfile_projector= args.weightfile_projector
	modelfile_predictor= args.modelfile_predictor
	weightfile_predictor= args.weightfile_predictor
	latentdim= args.latentdim
	add_maxpooling_layer= args.add_maxpooling_layer
	add_batchnorm_layer= args.add_batchnorm_layer
	add_leakyrelu= args.add_leakyrelu
	add_dense_layer= args.add_dense_layer	
	nfilters_cnn= [int(x.strip()) for x in args.nfilters_cnn.split(',')]
	kernsizes_cnn= [int(x.strip()) for x in args.kernsizes_cnn.split(',')]	
	strides_cnn= [int(x.strip()) for x in args.strides_cnn.split(',')]
	dense_layer_sizes= [int(x.strip()) for x in args.dense_layer_sizes.split(',')]
	dense_layer_activation= args.dense_layer_activation
	add_dropout_layer= args.add_dropout_layer
	dropout_rate= args.dropout_rate
	add_conv_dropout_layer= args.add_conv_dropout_layer
	conv_dropout_rate= args.conv_dropout_rate
	
	use_predefined_arch= args.use_predefined_arch
	predefined_arch= args.predefined_arch

	# - Train options
	optimizer= args.optimizer
	learning_rate= args.learning_rate
	batch_size= args.batch_size
	nepochs= args.nepochs
	weight_seed= args.weight_seed
	reproducible= args.reproducible
	validation_steps= args.validation_steps

	load_cv_data_in_batches= args.load_cv_data_in_batches
	multiprocessing= args.multiprocessing

	balance_classes_in_batch= args.balance_classes_in_batch

	class_probs_dict= {}
	if args.class_probs!="":
		try:
			class_probs_dict= json.loads(args.class_probs)
		except Exception as e:
			logger.error("Failed to convert class prob string to dict (err=%s)!" % (str(e)))
			return -1	

		print("== class_probs ==")
		print(class_probs_dict)

	# - Run options
	predict= args.predict

	# - Save options
	save_tb_embeddings= args.save_tb_embeddings
	nembeddings_save= args.nembeddings_save
	img_embedding_scale= args.img_embedding_scale
	shuffle_embeddings= args.shuffle_embeddings
	no_save_embeddings= args.no_save_embeddings

	#===============================
	#==  CREATE DATA PRE-PROCESSOR
	#===============================
	# - Pre-process stage order
	#   1) Channel resizer 
	#   2) Bkg sub
	#   3) Sigma clip/shift
	#   4) Scale
	#   5) Stretch (e.g. log transform, zscale)
	#   6) Mask ops (shrinker, border masking)
	#   7) Augmentation
	#   8) Resize
	#   9) min/max (abs) norm, standardize, mean shift
	logger.info("Create train data pre-processor ...")
	preprocess_stages= []

	if resize_chans:
		preprocess_stages.append(ChanResizer(nchans=nchan_resize))

	if subtract_bkg:
		preprocess_stages.append(BkgSubtractor(sigma=sigma_bkg, use_mask_box=use_box_mask_in_bkg, mask_fract=bkg_box_mask_fract, chid=bkg_chid))

	if clip_shift_data:
		preprocess_stages.append(SigmaClipShifter(sigma=sigma_clip, chid=clip_chid))

	if clip_data:
		preprocess_stages.append(SigmaClipper(sigma_low=sigma_clip_low, sigma_up=sigma_clip_up, chid=clip_chid))


	if scale_to_abs_max:
		preprocess_stages.append(AbsMaxScaler(use_mask_box=use_box_mask_in_chan_max_scaler, mask_fract=chan_max_scaler_box_mask_fract))

	if scale_to_selch_max:
		preprocess_stages.append(ChanMaxScaler(chref=chref, use_mask_box=use_box_mask_in_chan_max_scaler, mask_fract=chan_max_scaler_box_mask_fract))

	if scale:
		preprocess_stages.append(Scaler(scale_factors))

	if log_transform:
		preprocess_stages.append(LogStretcher(chid=log_transform_chid, minmaxnorm=log_transform_minmaxnorm, data_norm_min=log_transform_normmin, data_norm_max=log_transform_normmax, clip_neg=log_transform_clipneg))

	if zscale_stretch:
		preprocess_stages.append(ZScaleTransformer(contrasts=zscale_contrasts))

	if erode:
		preprocess_stages.append(MaskShrinker(kernel=erode_kernel))
	
	if chan3_preproc:
		preprocess_stages.append( Chan3Trasformer(sigma_clip_baseline=sigma_clip_baseline, sigma_clip_low=sigma_clip_low, sigma_clip_up=sigma_clip_up, zscale_contrast=zscale_contrasts[0]) )

	preprocess_stages.append(Augmenter(augmenter_choice=augmenter))

	if mask_borders:
		preprocess_stages.append(BorderMasker(mask_border_fract))
	
	if resize:
		preprocess_stages.append(Resizer(resize_size=resize_size, upscale=upscale, downscale_with_antialiasing=downscale_with_antialiasing, set_pad_val_to_min=set_pad_val_to_min))

	if normalize_minmax:
		preprocess_stages.append(MinMaxNormalizer())

	if normalize_absminmax:
		preprocess_stages.append(AbsMinMaxNormalizer())

	if scale_to_max:
		preprocess_stages.append(MaxScaler())

	#if scale_to_abs_max:
	#	preprocess_stages.append(AbsMaxScaler())

	if meanshift:
		preprocess_stages.append(Shifter(offsets=img_means))
	
	if standardize:
		preprocess_stages.append(Standardizer(means=img_means, sigmas=img_sigmas))
	
	#if chan_divide:
	#	preprocess_stages.append(ChanDivider(chref=chref))

	print("== PRE-PROCESSING STAGES (TRAIN) ==")
	print(preprocess_stages)

	dp= DataPreprocessor(preprocess_stages)

	# - Creating data pre-processor for validation/test data
	logger.info("Creating data pre-processor for validation data ...")
	preprocess_stages_val= []
	for stage in preprocess_stages:
		if isinstance(stage, Augmenter):
			continue
		preprocess_stages_val.append(stage)

	print("== PRE-PROCESSING STAGES (VAL) ==")
	print(preprocess_stages_val)

	dp_val= DataPreprocessor(preprocess_stages_val)

	#===============================
	#==  DATA GENERATOR
	#===============================
	# - Create train data generator
	dg= DataGenerator(filename=datalist, preprocessor=dp)

	logger.info("Reading datalist %s ..." % datalist)
	if dg.read_datalist()<0:
		logger.error("Failed to read input datalist!")
		return 1

	# - Create validation data generator
	dg_cv= None
	if datalist_cv!="":
		dg_cv= DataGenerator(filename=datalist_cv, preprocessor=dp_val)
		
		logger.info("Reading datalist_cv %s ..." % (datalist_cv))
		if dg_cv.read_datalist()<0:
			logger.error("Failed to read input datalist for validation!")
			return 1

	#===========================
	#==   BUILD MODEL
	#===========================
	byol= FeatExtractorByol(dg)
	byol.nchannels= nchannels
	byol.modelfile_encoder= modelfile_encoder
	byol.weightfile_encoder= weightfile_encoder
	byol.modelfile_projector= modelfile_projector
	byol.weightfile_projector= weightfile_projector
	byol.modelfile_predictor= modelfile_predictor
	byol.weightfile_predictor= weightfile_predictor
	byol.set_image_size(resize_size, resize_size)
	byol.latent_dim= latentdim

	byol.batch_size= batch_size
	byol.nepochs= nepochs
	byol.validation_steps= validation_steps
	byol.set_optimizer(optimizer, learning_rate)
	if reproducible:
		byol.set_reproducible_model()
	
	byol.add_max_pooling= add_maxpooling_layer
	byol.add_batchnorm= add_batchnorm_layer
	byol.add_leakyrelu= add_leakyrelu
	byol.add_dense= add_dense_layer
	byol.nfilters_cnn= nfilters_cnn
	byol.kernsizes_cnn= kernsizes_cnn
	byol.strides_cnn= strides_cnn
	byol.dense_layer_sizes= dense_layer_sizes
	byol.dense_layer_activation= dense_layer_activation
	byol.add_dropout_layer= add_dropout_layer
	byol.dropout_rate= dropout_rate
	byol.add_conv_dropout_layer= add_conv_dropout_layer
	byol.conv_dropout_rate= conv_dropout_rate

	byol.use_multiprocessing= multiprocessing
	byol.dg_cv= dg_cv
	byol.load_cv_data_in_batches= load_cv_data_in_batches

	byol.balance_classes= balance_classes_in_batch
	byol.class_probs= class_probs_dict
	byol.use_predefined_arch= use_predefined_arch
	byol.predefined_arch= predefined_arch

	byol.save_tb_embeddings= save_tb_embeddings
	byol.nembeddings_save= nembeddings_save
	byol.img_embedding_scale= img_embedding_scale
	byol.shuffle_embeddings= shuffle_embeddings
	byol.save_embeddings= True
	if no_save_embeddings:
		byol.save_embeddings= False

	# - Run train/predict
	if predict:
		status= byol.run_predict(modelfile_encoder, weightfile_encoder)
	else:
		status= byol.run_train(
			modelfile_encoder, weightfile_encoder, 
			modelfile_projector, weightfile_projector,
			modelfile_predictor, weightfile_predictor
		)
	
	if status<0:
		logger.error("BYOL run failed!")
		return 1
	
	return 0

###################
##   MAIN EXEC   ##
###################
if __name__ == "__main__":
	sys.exit(main())
