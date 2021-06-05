持续更新中ing

# whoisface

👶 👧 🧒 👦 👩 🧑 👨 👩‍🦱 🧑‍🦱 👨‍🦱 👩‍🦰 🧑‍🦰 👨‍🦰

⭐⭐ 基于树莓派的人脸识别系统设计与实现 ⭐⭐

👱‍♀️ 👱 👱‍♂️ 👩‍🦳 🧑‍🦳 👨‍🦳 👩‍🦲 🧑‍🦲 👨‍🦲 🧔 👵 🧓 👴

一个将毕设设计开源的项目，可以帮助很多需要将人脸识别应用在作业中的人 🌍。

这不仅仅是一个开放源代码的项目，也是一个教程向的开源项目。

--------------------


# 前言
## 为什么要做这个

因为我自己毕业设计做的就是人脸识别系统，但因为 😏 我比较强没有遇到什么问题，但是 🤡 室友比较菜，他的项目是做手写数字识别设计，我就顺手帮他做了，这个过程中，发现很多 Github 上的开源项目连基本的项目说明和运行环境都没有，像是随手上传一波代码就完事。我想这不能这么敷衍了事，所以就出这个 Github 开源项目，为世界的进步添砖盖瓦。

接下来会开源两个项目：
- 手写数字式识别 ✏️ 
- 人脸识别系统设计与实现 🧑‍🦱

本教程是人脸识别系统设计与实现  🧑‍🦱 

准备了一个 🐧 群，可加 `537131912`



# 项目介绍

## 概括

**本开源项目包含以下内容**:
- 基于树莓派运行 ❤️
- 开箱即用，包括安装配置环境、跑通代码 ❤️
- 完整的教程，项目的整体框架逻辑、代码讲解 ❤️
- 多种访问方式，支持 Web 浏览器访问、客户端访问 ❤️
- 简单易学 ❤️


------------------------------

**本开源项目有以下特点**：

- 硬件平台：树莓派4B（ 4GB ） ✔️
- 硬件设备：摄像头 ✔️
- 操作系统：Ubuntu18.04  ✔️
- 编程语言：python3 ✔️

### 技术选型说明


#### 硬件平台

选用的是树莓派作为硬件平台，我购买的是 4GB 版本，推荐你购买的时候最少购买 2GB 版本。
项目代码可以运行在个人电脑上，即不仅仅可以运行在树莓派上，可以跑在 PC 和 Mac 上面。
硬件设备需要一个摄像头。

> 最低要求是 2GB 版本，但是建议直接上 4GB 或者 8GB，不要为了省钱上低于 4GB 的，因为你可能安装一个 Gnome 桌面，它会直接吃掉 1.5GB 的内存（ RAM ），即开机即占用 1.5GB😟


#### 操作系统

选用的操作系统是 Ubuntu18.04 ARM架构的，具体架构版本是 aarch64，而不是树莓派官方提供的操作系统（官方系统的架构版本是 armv7l），同时项目代码可以运行在 window、 Mac、 Linux 等操作系统，因为项目中使用到的都是一些跨平台组件。


> 为什么选用 Ubuntu 作为操作系统而不是树莓派官方提供的镜像？
> 
> 因为最为一个优秀的 Coder 当然应该选用 Ubuntu 这种 Linux 发行版，而不是树莓派官方提供的发行版。
> 官方的发行版有以下缺点：
> - armv7l 架构的 32 位 版本，且不提供 64 位版本，身处 21 世纪，是在是想用 32 位版本，虽然用起来没有区别，64 位能做的 32 位都能做，但是32 位有一个限制是 64 位没有的 —— 最大内容使用上限 3.5 GB。
> - 官方镜像的 GUI 好丑好丑。

所以，如果是想用官方系统的小伙伴，出现的和本教程的差异性需要自己解决问题了，我建议你的直接用 光荣伟大而又正确的 Ubuntu 系统。

#### 编程语言

编程语言为什么选用 Python 我觉得是没有什么好疑问的，`人生苦短，我用 Python`，Python 在人工智能、深度学习领域大放异彩，没有比 Python 更适合做人脸识别应用项目的语言了。

> 当然 C++ 适合写人工智能、深度学习相关的基础部件，Python 就适合调用 C++ 、C 写的这些组件。前者造轮子，后者用轮子。


## 人脸识别系统设计与实现

人脸识别系统设计与实现，包含两部分内容 `人脸识别` + `系统设计` ，我相信没有人不知道人脸识别是什么，这项技术存在于我们生活中的每一个角落；但是对于系统设计，一定有很多人不知道，尤其是一些大学生，甚至是应届生。关于系统设计的答案在下面，请继续往下看 👇🏼 

### 什么是系统设计

TODO

### 人脸识别和系统设计相结合

看了上面的系统设计介绍，相信你已经明白，这里的 `系统设计` 并不是一个为了名字格式化、好看化加的限定词，而是一门试试实时的技术，一门让你成为架构师的技术。


### 终极目标与我的论文核心设计思路

我的论文下载地址：[人脸识别系统设计与实现](localhost)

TODO

