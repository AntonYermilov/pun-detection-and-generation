#!/usr/bin/env python3

from util import dataloader
import importlib
import sys


MIN_FEATURE = 1
MAX_FEATURE = 40


def main():
    if len(sys.argv) != 2:
        print("Expected one argument: <feature number>")
        sys.exit(1)

    feature_number = sys.argv[1]
    if not str.isnumeric(feature_number):
        print("Argument should be an integer")
        sys.exit(2)

    feature_number = int(feature_number)
    if feature_number < MIN_FEATURE or feature_number > MAX_FEATURE:
        print("Argument should be in range [{}, {}]".format(MIN_FEATURE, MAX_FEATURE))
        sys.exit(3)

    dataset = {'learn': dataloader.load_learn_dataset(),
               'test1': dataloader.load_test1_dataset(),
               'test2': dataloader.load_test2_dataset(),
               'validation': dataloader.load_validation_dataset()}

    module_name = 'feature' + str(feature_number)
    feature = importlib.import_module('features.' + module_name)

    print(module_name + ' calculation started')
    for target in ['test2', 'validation', 'test1', 'learn']:
        with open('outputs/{}/{}.out'.format(target, module_name), 'w') as output:
            for data in dataset[target]:
                text = data[1]
                result = feature.get_score(text)

                if isinstance(result, list):
                    for x in result:
                        output.write(str(x) + ' ')
                else:
                    output.write(str(result))
                output.write('\n')
    print(module_name + ' calculation finished')


if __name__ == '__main__':
    main()
