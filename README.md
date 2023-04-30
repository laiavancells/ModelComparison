# ModelComparison

## Description

This repository contains the code for four different machine learning models that predict speed (0.8 m/s, 1.2 m/s, 1.6 m/s) as a function of Ground Reaction Forces (GRFs). The models are:
- Decision Tree
- Random Forest
- Gradient Boosting
- Multilayer Perceptron

## Files
The following files are included in this repository:
- DecisionTree.ipynb
- RandomForest.ipynb
- GradientBoosting.ipynb
- MLPClassifier.ipynb

Each file contains the code for the corresponding machine learning model.

In addition, the following utility files are included:

- Parse_alg.py: This file contains functions for parsing the data used for training and testing the models.
- moment_loadsoal.py: This file contains functions for computing the moments and loads from the raw data.

### Usage

To use these models, run the corresponding Jupyter notebook file. You will need to have Python 3, Jupyter Notebook, and the necessary libraries installed on your system (note: the libraries vary depending on the model implemented).

Each notebook contains the necessary code for loading the data, training the model, and testing the model. You can modify the parameters and hyperparameters to experiment with different configurations.

## Results
After running each notebook, you can compare the results of each model to see which one performs best for your specific use case.

## Help

If you encounter any issues while using this project, try the following:

- Check that all dependencies are installed correctly
- Make sure that you are using the correct command to run the project

## Authors

Laia Vancells Lopez 

laia.vancellslopez@student.fairfield.edu

## Version History
* 0.1
    * Initial Release

## License

This project is licensed under the laiavancells License - see the LICENSE.md file for details

## Acknowledgments

I would like to thank Dr. Drazan and Dr. Bandara for their valuable feedback and contributions to this project. Their insights and expertise were instrumental in improving the quality of our work.

Note: This code has been written with a specific data file in mind (data_proc.mat), and may not work with other data files without modification.
