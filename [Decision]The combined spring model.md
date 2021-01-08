***

## The combined spring model

### The spring model property:  

semimajor & semiminor :   
$$
a = 1.5v_x \\
b = l_w
$$
The "elastic" force & energy :  
$$
F_{x,obj} = k_1\Delta d_{x,obj} \\
E_{x,obj} = \int_0^{\Delta d_{x,obj}}F_{x,obj}
$$
The equivalent forces depend on the relationships among the various movements of road users.
$$
F_{x,obj}=\frac{m_x v_x^2}{2d_{x,obj}}
$$

So, 
$$
k_1\Delta d_{obj1,obj2} = \frac{m_x v_x^2}{2}(\frac{1}{d_{x,obj1}}-\frac{1}{d_{x,obj2}}) \\
k_1 = \frac{m_xv_x^2}{2ad_{x,obj}}
$$

### Inertial force 

Inertial force is:
$$
F_{inertial,x} = m_x a_x = 2k_2\Delta d_x
$$
$ \Delta d_x $ denotes the length of the compressed spring.

Inertial force of the front vehicle and the spring force relate as follow:
$$
F_{inertial}=F_{ij}-F_{ji}
$$
So,
$$
k_2 = \frac{1}{2}k_1=\frac{m_jv_j^2}{4ad_{ji}}
$$

The completed formula are (8) - (14)
$$
\Delta x_{ji} = \frac{d_{ji}ab}{\sqrt{b^2x_i^2+a^2y_i^2}}-d_{ij}
$$
On the constant speed situation:
$$
F_{ij}=\frac{bm_jv_j^2}{2\sqrt{b^2x_i^2+a^2y_i^2}}-\frac{m_jv_j^2}{2a} \\
\theta = \arctan{\frac{y_i}{x_i}}
$$
On the acceleration driving conditions:
$$
F_{ji}=\frac{m_jv_j^2}{2ad_{ji}}\Delta　x_{j^{'}i}\\ \theta = \arctan \frac{y_j-y_i}{x_i+\Delta x_j -x_j}
$$

$$
\\
\Delta x_{j^{'}i} = \left( \frac{W_3-W_2\Delta x_j}{W_1+W_2}-x_i \right)\sqrt{1+\left( \frac{y_i}{x_i+\Delta x_j} \right)^2} 
$$

$$
W_1 = b^2(x_i+\Delta x_j)^2
$$

$$
\\ W_2 = a^2y_i^2
$$

$$
\\  W_3 = \sqrt{W_2^2\Delta x_j^2+(W_1+W_2)(W_1a^2-W_2\Delta x_j^2)}
$$

### The behavior decision making model 

The last action model can be express by :
$$
S= \int_{t_0}^{t_f}L dt = \int_{t_0}^{t_f}(T-U)dt
$$
$ T $ means kinetic energy, $U$ means interactive energy.

The mathematical model of multi-objective decision making :
$$
G_i=m_ig_h
$$

$$
g_h = k\frac{v_{der}}{v_{limit}}g
$$

$k$ means constant, $v_{der}$  denotes expected speed,  $v_{limit}$  denotes limit speed, 


