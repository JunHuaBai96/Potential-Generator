# Potential-Generator
基于Zhou的最全的合金势函数生成器GUI版本

##在做合金的动力学模拟的时候, 大家经常遇到的一个问题就是合金的势函数不好找, 但是幸好Zhou大佬在2004年的一篇PRB中给出了高达16种元素之间相互作用的势函数生成方法以及Fortran代码[1], 之后香港城市大学的赵士俊[2]老师以及一篇08年的PRB[3]中分别给出了V和Cr的相关参数, 使得这个势函数中元素种类增加到了18种.

为了方便大家的势函数使用, 我利用python中的TKinter库将Zhou老师的相关工作整合进了一个软件并且有GUI界面. 该软件提供了最多六种金属元素之间的eam/alloy势函数文件的拟合:![image](https://github.com/JunHuaBai96/Potential-Generator/assets/102909786/10ea3aab-2fd5-41c8-af04-4826e53c31c8)

这里我们以拟合CuZrAg的合金势函数为例, 选择对应的元素, 然后点击生成势函数文件, 即可在软件的工作目录, 也就是对应的exe文件的目录下面找到对应的势函数文件：![image](https://github.com/JunHuaBai96/Potential-Generator/assets/102909786/3336e42d-e4c1-45f8-83e1-c83040828579)
    
此外, 该程序具有较强的容错能力, 以上图为例, 即使我们不按顺序, 比如元素一为Cu, 三为Ag, 六为Zr, 依然可以正确生成对应的势函数文件:![image](https://github.com/JunHuaBai96/Potential-Generator/assets/102909786/246b4ce2-bfeb-4354-85d2-b70cc3b857c5)

如果同学们在选择元素的时候一不小心选择了2个相同元素, 程序也可以正确处理:![image](https://github.com/JunHuaBai96/Potential-Generator/assets/102909786/d4074505-1de8-4dc5-9f18-547d180679f4)

如果没有选择元素, 软件会给出对应报错:![image](https://github.com/JunHuaBai96/Potential-Generator/assets/102909786/2530c506-7631-40d3-8628-45d89b03aa3f)

此外还提供了中英对照表以方便大家使用：![image](https://github.com/JunHuaBai96/Potential-Generator/assets/102909786/48aef8f5-3941-4ed4-bc53-547e4be24d87)

##引用文献:
[1] Misfit-energy-increasing dislocations in vapor-deposited CoFe/NiFe multilayers
[2] Defect accumulation and evolution in refractory multi-principal element alloys
[3] Computational study of the generation of crystal defects in a bcc metal target irradiated by short laser pulses  
