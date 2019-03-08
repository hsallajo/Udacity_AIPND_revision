#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: S. Huopone
# DATE CREATED: Mar-7, 2019
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
def print_results(results_dict, results_stats_dict, model,
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """
    print("\n")
    print("# ************************************************")
    print("# Model arch: {}".format(model))
    print("# Number of images: {}".format(results_stats_dict["n_count_num_images"]))
    print("# Number of Dog images: {}".format(results_stats_dict["n_count_num_dog_imgs"]))
    print("# Number of 'Not-a' Dog images: {}".format(results_stats_dict["n_count_num_not_dog_imgs"]))

    for item, val in results_stats_dict.items():
        if item[0] == 'p':
            print("# {}: {}".format(item, val))

    print("#\n")
    print("# Print misclassifications: {}".format(print_incorrect_dogs))

    if print_incorrect_dogs:
        # Misclassified dogs: labels disagree on whether or not an image is of a dog
        print("# Number of misclassified dogs: {}".format( \
            results_stats_dict['n_count_num_images'] - \
            results_stats_dict['n_count_num_corr_dog_matches'] - \
            results_stats_dict['n_count_num_corr_non_dog_matches']))
        for misc_key, misc_val in results_dict.items():
            if sum(misc_val[3:]) == 1:
                print("# Misclassified: {}: '{}' vs '{}'".format(misc_key, misc_val[0], misc_val[1]))

    print("#\n")
    print("# Print misclassifications of breeds: {}".format(print_incorrect_breed))
    if print_incorrect_breed:
        count = 0
        # Misclassified breeds of dogs: both labels indicate that the image is a dog; but, labels aren't in agreement regarding the dog's breed
        for inc_breed_key, inc_breed_val in results_dict.items():
            if sum(results_dict[inc_breed_key][3:]) == 2 and results_dict[inc_breed_key][2] == 0:
                count += 1
                print("# Misclassified breed: {}: '{}' vs '{}'".format(inc_breed_key, inc_breed_val[0], inc_breed_val[1]))
        print("# Misclassified breeds of dogs: {} ".format(count))
