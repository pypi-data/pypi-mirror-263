from iminuit import Minuit
import sympy as sp


###########################
### NO COVARIANCE #########
###########################
def make_sigmas(parametri):
    sigmas = []

    for var in parametri:
        sigmas.append(f'sigma_{var}')

    return sp.symbols(sigmas)

def prop_no_cov(parametri:str, formula:str):

    #convert from str to sympy
    parametri = sp.sympify(parametri)
    formula = sp.simplify(formula)
    sigmas = make_sigmas(sp.sympify(parametri))
    i,exp = 0,0

    for val in parametri:

        #sum squared partial derivatives and sigmas
        exp += sp.diff(formula,val)**2 * sigmas[i]**2
        i+=1

    #sqrt the expression
    exp = sp.sqrt(exp)

    return sp.simplify(exp)

def evaluate(prop_formula:str, Minuit_values:dict, Minuit_errors:dict, x_val):

    #convert minuit values method to dict
    params = Minuit_values.keys()

    #sustitute numerical values
    expr = prop_formula.subs(Minuit_values)

    for val in Minuit_errors:

        #substitute numerical for sigmas
        expr = expr.subs(f'sigma_{val}', Minuit_errors[val])

    expr = expr.subs(sp.symbols('x'), x_val)

    return expr

###########################
### WITH COVARIANCE #######
###########################

def MatToDict(array):
  '''Covariance Array to dictionary conversion'''

  dic = {}
  variables = m.values.to_dict().keys()
  indexes = ['sigma_'+f'{var1}{var2}' for var1 in variables for var2 in variables]
  values = []

  for i in array.tolist():
    for j in i:
      values.append(j)

  for i in range(len(indexes)):
    dic[indexes[i]] = values[i]

  return dic

############################
##### CLASS ################
############################

class ExtendedMinuit(Minuit):

    def __init__(self, fcn, *args, grad=None, name=None, **kwds):
        super().__init__(fcn, *args, grad=grad, name=name, **kwds)

    def prop_errors(self, params:str, formula:str, x_val, eval=False) -> tuple['expr':str,'value':float]:
        """
        Error Propagation trough given formula like 'y = a * (b+x*c)'

        Usage
        =====
            ``params``  : string like: 'a,b,c'
            ``formula`` : string like: 'a * (b+x*c)'

        Return
        ======

        ``if``

        Credits
        =======
        made by ``~Edi~``
        """

        #formula for errors
        expr = prop_no_cov(params, formula)

        #numerical value for x_val
        value = evaluate(expr, self.values.to_dict(), self.errors.to_dict(), x_val)

        if eval == True:
            return str(value)

        else:
            return sp.latex(expr)

    def prop_cov(self, variables:str, formula:str, x_val:float=None, eval:bool=True):
        '''
        Function for calculating propagated uncertainty with covariance give Iminuit Class and interpolation formula

        Usage
        ======
        ``variables`` : string of type 'a,b,c,d'
        ``formula`` : string of type 'a*x^2+b*x+c'
        ``x_val`` : any value for x ( can be omitted )

        >>> a = prop_cov('a,b,c,d', 'a*x^2+b*x+c' , m , x_val=2, eval=False)
        >>> Latex(a)

        Return Conditions
        =================

        ``eval`` -> ``if`` True: function returns sigma value
        ``eval`` -> ``if`` False: function returns sigma formula

        Needed Libs
        ===========

        >>> import sympy as sp
        >>> import iminuit.Minuit
        >>> from IPython.display import Latex

        Credits
        =======
        made by ``~Edi~``
        '''


        vars = sp.sympify(variables)
        formula = sp.simplify(formula)

        covariances = MatToDict(self.covariance)
        values = self.values.to_dict()

        exp = 0
        for var1 in vars:
            for var2 in vars:

                exp += sp.diff(formula,var1)*sp.diff(formula,var2) * sp.sympify(f'sigma_{var1}{var2}')

        if eval == True:
            exp = exp.subs(values)
            exp = exp.subs(covariances)
            if x_val != None:
                exp = exp.subs(sp.symbols('x'), x_val)
                return '\sigma_y = ' + sp.latex(sp.sqrt(exp))

        else:
            return '\sigma_y = ' + sp.latex(sp.sqrt(exp))


if __name__ == '__main__':
    from iminuit.cost import*
    import numpy as np
    import matplotlib.pyplot as plt

    def f(x,a,b,c):
        return a*x**2+b*x+c

    x = np.linspace(0,10)
    y = [f(i,1,2,3)+np.random.uniform(0,1) for i in x]

    plt.scatter(x,y)
    # plt.show()

    c = LeastSquares(x,y,0.01,f)
    m = ExtendedMinuit(c,a=1,b=1,c=1)
    m.migrad()
    val = m.prop_errors('a,b,c','a*x**2+b*x+c',2,True)
    print(val)
    print(m)