#!/usr/bin/env python3

from util import dataloader


MIN_FEATURE = 1
MAX_FEATURE = 40


def main():
    dataset = {'learn': dataloader.load_learn_dataset(),
               'test1': dataloader.load_test1_dataset(),
               'test2': dataloader.load_test2_dataset(),
               'validation': dataloader.load_validation_dataset()}

    for target in ['test2', 'validation', 'test1', 'learn']:
        vectors = []
        for data in dataset[target]:
            label = data[0]
            vectors.append({'label': label, 'vector': []})

        for feature_number in range(MIN_FEATURE, MAX_FEATURE + 1):
            module_name = 'feature' + str(feature_number)
            with open('outputs/{}/{}.out'.format(target, module_name), 'r') as input:
                lines = input.readlines()
                for i in range(len(lines)):
                    values = list(map(float, lines[i].split()))
                    vectors[i]['vector'] += values

        with open('svm_vectors/{}/vectors.out'.format(target), 'w') as output:
            for vector in vectors:
                output.write(str(vector['label']))
                id = 1
                for value in vector['vector']:
                    output.write(' ' + str(id) + ':' + str(value))
                    id += 1
                output.write('\n')


if __name__ == '__main__':
    main()
