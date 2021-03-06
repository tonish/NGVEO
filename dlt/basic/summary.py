from dlt.basic.metrics import mean_absolute_error,balanced_accuracy

color_white = '\033[0m'
color_blue = '\033[94m'
color_green = '\033[92m'

def regression_summary(iteration, mode, data, target, prediction, loss=None):

    if loss is None:

        print(color_blue, mode, str(iteration).ljust(4),  '- mean absolute error:', mean_absolute_error(prediction, target), color_white)
    else:
        print(color_green,mode, str(iteration).ljust(4), ' - loss:', str(loss).ljust(14),  'mean absolute error:', mean_absolute_error(prediction, target), color_white)
    return  mean_absolute_error(prediction, target)

def classification_summary(iteration, mode, data, target, prediction, loss=None):

    if loss is None:
        print(color_blue, mode, str(iteration).ljust(4),  '- class balanced accuracy:', balanced_accuracy(prediction, target), color_white)
    else:
        print(color_green,mode, str(iteration).ljust(4), ' - loss:', str(loss).ljust(14),  'class balanced accuracy:', balanced_accuracy(prediction, target), color_white)

    return balanced_accuracy(prediction, target)