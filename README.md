python3 -c "import platform; print(platform.machine())"
dpkg -l | grep -E 'nvidia-l4t-cuda|nvidia-cudnn|tensorrt|nvinfer'
nvidia-smi
aarch64
ii  libnvinfer-bin                                    10.3.0.30-1+cuda12.5                        arm64        TensorRT binaries
ii  libnvinfer-dev                                    10.3.0.30-1+cuda12.5                        arm64        TensorRT development libraries
ii  libnvinfer-dispatch-dev                           10.3.0.30-1+cuda12.5                        arm64        TensorRT development dispatch runtime libraries
ii  libnvinfer-dispatch10                             10.3.0.30-1+cuda12.5                        arm64        TensorRT dispatch runtime library
ii  libnvinfer-headers-dev                            10.3.0.30-1+cuda12.5                        arm64        TensorRT development headers
ii  libnvinfer-headers-plugin-dev                     10.3.0.30-1+cuda12.5                        arm64        TensorRT plugin headers
ii  libnvinfer-lean-dev                               10.3.0.30-1+cuda12.5                        arm64        TensorRT lean runtime libraries
ii  libnvinfer-lean10                                 10.3.0.30-1+cuda12.5                        arm64        TensorRT lean runtime library
ii  libnvinfer-plugin-dev                             10.3.0.30-1+cuda12.5                        arm64        TensorRT plugin libraries
ii  libnvinfer-plugin10                               10.3.0.30-1+cuda12.5                        arm64        TensorRT plugin libraries
ii  libnvinfer-samples                                10.3.0.30-1+cuda12.5                        all          TensorRT samples
ii  libnvinfer-vc-plugin-dev                          10.3.0.30-1+cuda12.5                        arm64        TensorRT vc-plugin library
ii  libnvinfer-vc-plugin10                            10.3.0.30-1+cuda12.5                        arm64        TensorRT vc-plugin library
ii  libnvinfer10                                      10.3.0.30-1+cuda12.5                        arm64        TensorRT runtime libraries
ii  nvidia-cudnn                                      6.2.1+b38                                   arm64        NVIDIA CUDNN Meta Package
ii  nvidia-cudnn-dev                                  6.2.1+b38                                   arm64        NVIDIA CUDNN dev Meta Package
ii  nvidia-l4t-cuda                                   36.4.7-20250918154033                       arm64        NVIDIA CUDA Package
ii  nvidia-l4t-cuda-utils                             36.4.7-20250918154033                       arm64        NVIDIA CUDA utilities
ii  nvidia-l4t-cudadebuggingsupport                   12.6-34622040.0                             arm64        NVIDIA CUDA Debugger Support Package
ii  nvidia-tensorrt                                   6.2.1+b38                                   arm64        NVIDIA TensorRT Meta Package
ii  nvidia-tensorrt-dev                               6.2.1+b38                                   arm64        NVIDIA TensorRT dev Meta Package
ii  python3-libnvinfer                                10.3.0.30-1+cuda12.5                        arm64        Python 3 bindings for TensorRT standard runtime
ii  python3-libnvinfer-dev                            10.3.0.30-1+cuda12.5                        arm64        Python 3 development package for TensorRT standard runtime
ii  python3-libnvinfer-dispatch                       10.3.0.30-1+cuda12.5                        arm64        Python 3 bindings for TensorRT dispatch runtime
ii  python3-libnvinfer-lean                           10.3.0.30-1+cuda12.5                        arm64        Python 3 bindings for TensorRT lean runtime
ii  tensorrt                                          10.3.0.30-1+cuda12.5                        arm64        Meta package for TensorRT
ii  tensorrt-libs                                     10.3.0.30-1+cuda12.5                        arm64        Meta package for TensorRT runtime libraries
Tue Apr 14 12:29:44 2026       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 540.4.0                Driver Version: 540.4.0      CUDA Version: 12.6     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  Orin (nvgpu)                  N/A  | N/A              N/A |                  N/A |
| N/A   N/A  N/A               N/A /  N/A | Not Supported        |     N/A          N/A |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found       
