[[package]]
name = "click"
version = "8.0.3"
description = "Composable command line interface toolkit"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.4"
description = "Cross-platform colored terminal text."
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[[package]]
name = "elements"
version = "0.3.2"
description = "Building blocks for productive research."
category = "main"
optional = false
python-versions = "*"

[package.dependencies]
imageio = "*"
numpy = "*"

[[package]]
name = "imageio"
version = "2.9.0"
description = "Library for reading and writing a wide range of image, video, scientific, and volumetric data formats."
category = "main"
optional = false
python-versions = ">=3.5"

[package.dependencies]
numpy = "*"
pillow = "*"

[package.extras]
ffmpeg = ["imageio-ffmpeg"]
fits = ["astropy"]
full = ["astropy", "gdal", "imageio-ffmpeg", "itk"]
gdal = ["gdal"]
itk = ["itk"]

[[package]]
name = "numpy"
version = "1.21.1"
description = "NumPy is the fundamental package for array computing with Python."
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "pillow"
version = "8.4.0"
description = "Python Imaging Library (Fork)"
category = "main"
optional = false
python-versions = ">=3.6"

[metadata]
lock-version = "1.1"
python-versions = "^3.8"
content-hash = "19754cd1f82209c292dbad9f3505b2d813c14e1e58ad49e8e2a104d4a43ab9ac"

[metadata.files]
click = [
    {file = "click-8.0.3-py3-none-any.whl", hash = "sha256:353f466495adaeb40b6b5f592f9f91cb22372351c84caeb068132442a4518ef3"},
    {file = "click-8.0.3.tar.gz", hash = "sha256:410e932b050f5eed773c4cda94de75971c89cdb3155a72a0831139a79e5ecb5b"},
]
colorama = [
    {file = "colorama-0.4.4-py2.py3-none-any.whl", hash = "sha256:9f47eda37229f68eee03b24b9748937c7dc3868f906e8ba69fbcbdd3bc5dc3e2"},
    {file = "colorama-0.4.4.tar.gz", hash = "sha256:5941b2b48a20143d2267e95b1c2a7603ce057ee39fd88e7329b0c292aa16869b"},
]
elements = [
    {file = "elements-0.3.2.tar.gz", hash = "sha256:15cbd8cde180e1012d264199d44f07957d19cba650ecb4280691960c57cf4f98"},
]
imageio = [
    {file = "imageio-2.9.0-py3-none-any.whl", hash = "sha256:3604d751f03002e8e0e7650aa71d8d9148144a87daf17cb1f3228e80747f2e6b"},
    {file = "imageio-2.9.0.tar.gz", hash = "sha256:52ddbaeca2dccf53ba2d6dec5676ca7bc3b2403ef8b37f7da78b7654bb3e10f0"},
]
numpy = [
    {file = "numpy-1.21.1-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:38e8648f9449a549a7dfe8d8755a5979b45b3538520d1e735637ef28e8c2dc50"},
    {file = "numpy-1.21.1-cp37-cp37m-manylinux_2_12_i686.manylinux2010_i686.whl", hash = "sha256:fd7d7409fa643a91d0a05c7554dd68aa9c9bb16e186f6ccfe40d6e003156e33a"},
    {file = "numpy-1.21.1-cp37-cp37m-manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:a75b4498b1e93d8b700282dc8e655b8bd559c0904b3910b144646dbbbc03e062"},
    {file = "numpy-1.21.1-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1412aa0aec3e00bc23fbb8664d76552b4efde98fb71f60737c83efbac24112f1"},
    {file = "numpy-1.21.1-cp37-cp37m-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:e46ceaff65609b5399163de5893d8f2a82d3c77d5e56d976c8b5fb01faa6b671"},
    {file = "numpy-1.21.1-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.whl", hash = "sha256:c6a2324085dd52f96498419ba95b5777e40b6bcbc20088fddb9e8cbb58885e8e"},
    {file = "numpy-1.21.1-cp37-cp37m-win32.whl", hash = "sha256:73101b2a1fef16602696d133db402a7e7586654682244344b8329cdcbbb82172"},
    {file = "numpy-1.21.1-cp37-cp37m-win_amd64.whl", hash = "sha256:7a708a79c9a9d26904d1cca8d383bf869edf6f8e7650d85dbc77b041e8c5a0f8"},
    {file = "numpy-1.21.1-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:95b995d0c413f5d0428b3f880e8fe1660ff9396dcd1f9eedbc311f37b5652e16"},
    {file = "numpy-1.21.1-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:635e6bd31c9fb3d475c8f44a089569070d10a9ef18ed13738b03049280281267"},
    {file = "numpy-1.21.1-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:4a3d5fb89bfe21be2ef47c0614b9c9c707b7362386c9a3ff1feae63e0267ccb6"},
    {file = "numpy-1.21.1-cp38-cp38-manylinux_2_12_i686.manylinux2010_i686.whl", hash = "sha256:8a326af80e86d0e9ce92bcc1e65c8ff88297de4fa14ee936cb2293d414c9ec63"},
    {file = "numpy-1.21.1-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:791492091744b0fe390a6ce85cc1bf5149968ac7d5f0477288f78c89b385d9af"},
    {file = "numpy-1.21.1-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0318c465786c1f63ac05d7c4dbcecd4d2d7e13f0959b01b534ea1e92202235c5"},
    {file = "numpy-1.21.1-cp38-cp38-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:9a513bd9c1551894ee3d31369f9b07460ef223694098cf27d399513415855b68"},
    {file = "numpy-1.21.1-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl", hash = "sha256:91c6f5fc58df1e0a3cc0c3a717bb3308ff850abdaa6d2d802573ee2b11f674a8"},
    {file = "numpy-1.21.1-cp38-cp38-win32.whl", hash = "sha256:978010b68e17150db8765355d1ccdd450f9fc916824e8c4e35ee620590e234cd"},
    {file = "numpy-1.21.1-cp38-cp38-win_amd64.whl", hash = "sha256:9749a40a5b22333467f02fe11edc98f022133ee1bfa8ab99bda5e5437b831214"},
    {file = "numpy-1.21.1-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:d7a4aeac3b94af92a9373d6e77b37691b86411f9745190d2c351f410ab3a791f"},
    {file = "numpy-1.21.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:d9e7912a56108aba9b31df688a4c4f5cb0d9d3787386b87d504762b6754fbb1b"},
    {file = "numpy-1.21.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:25b40b98ebdd272bc3020935427a4530b7d60dfbe1ab9381a39147834e985eac"},
    {file = "numpy-1.21.1-cp39-cp39-manylinux_2_12_i686.manylinux2010_i686.whl", hash = "sha256:8a92c5aea763d14ba9d6475803fc7904bda7decc2a0a68153f587ad82941fec1"},
    {file = "numpy-1.21.1-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:05a0f648eb28bae4bcb204e6fd14603de2908de982e761a2fc78efe0f19e96e1"},
    {file = "numpy-1.21.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f01f28075a92eede918b965e86e8f0ba7b7797a95aa8d35e1cc8821f5fc3ad6a"},
    {file = "numpy-1.21.1-cp39-cp39-win32.whl", hash = "sha256:88c0b89ad1cc24a5efbb99ff9ab5db0f9a86e9cc50240177a571fbe9c2860ac2"},
    {file = "numpy-1.21.1-cp39-cp39-win_amd64.whl", hash = "sha256:01721eefe70544d548425a07c80be8377096a54118070b8a62476866d5208e33"},
    {file = "numpy-1.21.1-pp37-pypy37_pp73-manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:2d4d1de6e6fb3d28781c73fbde702ac97f03d79e4ffd6598b880b2d95d62ead4"},
    {file = "numpy-1.21.1.zip", hash = "sha256:dff4af63638afcc57a3dfb9e4b26d434a7a602d225b42d746ea7fe2edf1342fd"},
]
pillow = [
    {file = "Pillow-8.4.0-cp310-cp310-macosx_10_10_universal2.whl", hash = "sha256:81f8d5c81e483a9442d72d182e1fb6dcb9723f289a57e8030811bac9ea3fef8d"},
    {file = "Pillow-8.4.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:3f97cfb1e5a392d75dd8b9fd274d205404729923840ca94ca45a0af57e13dbe6"},
    {file = "Pillow-8.4.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:eb9fc393f3c61f9054e1ed26e6fe912c7321af2f41ff49d3f83d05bacf22cc78"},
    {file = "Pillow-8.4.0-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d82cdb63100ef5eedb8391732375e6d05993b765f72cb34311fab92103314649"},
    {file = "Pillow-8.4.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:62cc1afda735a8d109007164714e73771b499768b9bb5afcbbee9d0ff374b43f"},
    {file = "Pillow-8.4.0-cp310-cp310-win32.whl", hash = "sha256:e3dacecfbeec9a33e932f00c6cd7996e62f53ad46fbe677577394aaa90ee419a"},
    {file = "Pillow-8.4.0-cp310-cp310-win_amd64.whl", hash = "sha256:620582db2a85b2df5f8a82ddeb52116560d7e5e6b055095f04ad828d1b0baa39"},
    {file = "Pillow-8.4.0-cp36-cp36m-macosx_10_10_x86_64.whl", hash = "sha256:1bc723b434fbc4ab50bb68e11e93ce5fb69866ad621e3c2c9bdb0cd70e345f55"},
    {file = "Pillow-8.4.0-cp36-cp36m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:72cbcfd54df6caf85cc35264c77ede902452d6df41166010262374155947460c"},
    {file = "Pillow-8.4.0-cp36-cp36m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:70ad9e5c6cb9b8487280a02c0ad8a51581dcbbe8484ce058477692a27c151c0a"},
    {file = "Pillow-8.4.0-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:25a49dc2e2f74e65efaa32b153527fc5ac98508d502fa46e74fa4fd678ed6645"},
    {file = "Pillow-8.4.0-cp36-cp36m-win32.whl", hash = "sha256:93ce9e955cc95959df98505e4608ad98281fff037350d8c2671c9aa86bcf10a9"},
    {file = "Pillow-8.4.0-cp36-cp36m-win_amd64.whl", hash = "sha256:2e4440b8f00f504ee4b53fe30f4e381aae30b0568193be305256b1462216feff"},
    {file = "Pillow-8.4.0-cp37-cp37m-macosx_10_10_x86_64.whl", hash = "sha256:8c803ac3c28bbc53763e6825746f05cc407b20e4a69d0122e526a582e3b5e153"},
    {file = "Pillow-8.4.0-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c8a17b5d948f4ceeceb66384727dde11b240736fddeda54ca740b9b8b1556b29"},
    {file = "Pillow-8.4.0-cp37-cp37m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:1394a6ad5abc838c5cd8a92c5a07535648cdf6d09e8e2d6df916dfa9ea86ead8"},
    {file = "Pillow-8.4.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:792e5c12376594bfcb986ebf3855aa4b7c225754e9a9521298e460e92fb4a488"},
    {file = "Pillow-8.4.0-cp37-cp37m-win32.whl", hash = "sha256:d99ec152570e4196772e7a8e4ba5320d2d27bf22fdf11743dd882936ed64305b"},
    {file = "Pillow-8.4.0-cp37-cp37m-win_amd64.whl", hash = "sha256:7b7017b61bbcdd7f6363aeceb881e23c46583739cb69a3ab39cb384f6ec82e5b"},
    {file = "Pillow-8.4.0-cp38-cp38-macosx_10_10_x86_64.whl", hash = "sha256:d89363f02658e253dbd171f7c3716a5d340a24ee82d38aab9183f7fdf0cdca49"},
    {file = "Pillow-8.4.0-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:0a0956fdc5defc34462bb1c765ee88d933239f9a94bc37d132004775241a7585"},
    {file = "Pillow-8.4.0-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5b7bb9de00197fb4261825c15551adf7605cf14a80badf1761d61e59da347779"},
    {file = "Pillow-8.4.0-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:72b9e656e340447f827885b8d7a15fc8c4e68d410dc2297ef6787eec0f0ea409"},
    {file = "Pillow-8.4.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a5a4532a12314149d8b4e4ad8ff09dde7427731fcfa5917ff16d0291f13609df"},
    {file = "Pillow-8.4.0-cp38-cp38-win32.whl", hash = "sha256:82aafa8d5eb68c8463b6e9baeb4f19043bb31fefc03eb7b216b51e6a9981ae09"},
    {file = "Pillow-8.4.0-cp38-cp38-win_amd64.whl", hash = "sha256:066f3999cb3b070a95c3652712cffa1a748cd02d60ad7b4e485c3748a04d9d76"},
    {file = "Pillow-8.4.0-cp39-cp39-macosx_10_10_x86_64.whl", hash = "sha256:5503c86916d27c2e101b7f71c2ae2cddba01a2cf55b8395b0255fd33fa4d1f1a"},
    {file = "Pillow-8.4.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:4acc0985ddf39d1bc969a9220b51d94ed51695d455c228d8ac29fcdb25810e6e"},
    {file = "Pillow-8.4.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0b052a619a8bfcf26bd8b3f48f45283f9e977890263e4571f2393ed8898d331b"},
    {file = "Pillow-8.4.0-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:493cb4e415f44cd601fcec11c99836f707bb714ab03f5ed46ac25713baf0ff20"},
    {file = "Pillow-8.4.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b8831cb7332eda5dc89b21a7bce7ef6ad305548820595033a4b03cf3091235ed"},
    {file = "Pillow-8.4.0-cp39-cp39-win32.whl", hash = "sha256:5e9ac5f66616b87d4da618a20ab0a38324dbe88d8a39b55be8964eb520021e02"},
    {file = "Pillow-8.4.0-cp39-cp39-win_amd64.whl", hash = "sha256:3eb1ce5f65908556c2d8685a8f0a6e989d887ec4057326f6c22b24e8a172c66b"},
    {file = "Pillow-8.4.0-pp36-pypy36_pp73-macosx_10_10_x86_64.whl", hash = "sha256:ddc4d832a0f0b4c52fff973a0d44b6c99839a9d016fe4e6a1cb8f3eea96479c2"},
    {file = "Pillow-8.4.0-pp36-pypy36_pp73-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:9a3e5ddc44c14042f0844b8cf7d2cd455f6cc80fd7f5eefbe657292cf601d9ad"},
    {file = "Pillow-8.4.0-pp36-pypy36_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c70e94281588ef053ae8998039610dbd71bc509e4acbc77ab59d7d2937b10698"},
    {file = "Pillow-8.4.0-pp37-pypy37_pp73-macosx_10_10_x86_64.whl", hash = "sha256:3862b7256046fcd950618ed22d1d60b842e3a40a48236a5498746f21189afbbc"},
    {file = "Pillow-8.4.0-pp37-pypy37_pp73-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:a4901622493f88b1a29bd30ec1a2f683782e57c3c16a2dbc7f2595ba01f639df"},
    {file = "Pillow-8.4.0-pp37-pypy37_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:84c471a734240653a0ec91dec0996696eea227eafe72a33bd06c92697728046b"},
    {file = "Pillow-8.4.0-pp37-pypy37_pp73-win_amd64.whl", hash = "sha256:244cf3b97802c34c41905d22810846802a3329ddcb93ccc432870243211c79fc"},
    {file = "Pillow-8.4.0.tar.gz", hash = "sha256:b8e2f83c56e141920c39464b852de3719dfbfb6e3c99a2d8da0edf4fb33176ed"},
]
