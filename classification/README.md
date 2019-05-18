# Classification !
Pytorch code for classification on CIFAR-10/100 and ImageNet 

## Features
* Unified interface for different network architectures
* Multi-Node-GPU support
* Save as the file with Acc/Loss 

## Results

### CIFAR
Top1 error rate on the CIFAR-10/100 benchmarks are reported. You may get different results when training your models with different random seed.
Note that the number of parameters are computed on the CIFAR-10 dataset.

| Model                     | Params (M)         |  CIFAR-10 (%)      | CIFAR-100 (%)      |
| -------------------       | ------------------ | ------------------ | ------------------ |
| alexnet                   | 2.47               | 74.09              | 38.11              |
| vgg16                     | -                  | 89.83              | 54.89              |
| vgg19_bn                  | 20.04              | 92.80              | 71.89              |
| ResNet-20                 | -                  | 91.70              | 67.47              |
| ResNet-56                 | -                  | 92.88              | 70.86              |
| ResNet-110                | 1.70               | 91.54              | 72.20              |
| ResNet-1202               | -                  | 91.80              | 66.63              |
| PreResNet-110             | 1.70               | 93.89              | 72.65              |
| WRN-28-10 (drop 0.3)      | 36.48              | 94.25              | 77.77              |
| ResNeXt-29, 8x64          | 34.43              | 96.08              | 81.48              |
| ResNeXt-29, 16x64         | 68.16              | 96.69              | 81.69              |
| DenseNet-BC (L=100, k=12) | 0.77               | 95.02              | 77.17              |
| DenseNet-BC (L=190, k=40) | 25.62              | 96.72              | 81.95              |
| Mobilenet                 | -                  | 92.00              | 67.6               |
| MobilnetV2                | -                  | 93.90              | 75.61              |
| ShufflenetV2              | -                  | 92.83              | 72.3               |

