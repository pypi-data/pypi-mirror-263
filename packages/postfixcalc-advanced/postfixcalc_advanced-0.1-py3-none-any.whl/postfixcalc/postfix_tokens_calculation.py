from postfixcalc_advanced.avaliable_math_logic_operators import OPERATORs_DICT_func_1, OPERATORs_PRECEDENCE_DICT, \
    OPERATORs_DICT_binary_between, OPERATORs_DICT_math_U

from postfixcalc_advanced.postfix4tokens import string2postfix_tuple, tokenize, tokensPostfixing
import math

def postfixTokenCalc(tokens: tuple, DICT_VARS=None):
    """
    returns calculation result
    :param tokens: floats, vars, operators, functions
    :param DICT_VARS:
    :return: number
    """
    #print(f'postfixTokenCalc tuple = {tokens}')
    if DICT_VARS is None:
        DICT_VARS = {}
    stack_l = []
    if tokens is None:
        return None
    for t in tokens:
        #print('t in tokens: ', t)
        if type(t) is float or type(t) is int or type(t) is complex: # todo int and complex not needed in CNC
            stack_l.append(t)
        elif t in OPERATORs_PRECEDENCE_DICT:
            right = stack_l.pop(-1)
            if t in OPERATORs_DICT_binary_between:
                if len(stack_l) == 0 and (t == '-' or t == '+'):
                    stack_l.append(right) if t == '+' else stack_l.append(-right)
                else:
                    if len(stack_l) == 0:
                        if t == '=':
                            return right
                        else:
                            return None
                    left = stack_l.pop(-1)
                    if left is not None and right is not None:
                        stack_l.append(OPERATORs_DICT_binary_between[t](left, right))
                    else:
                        print('None in {} or {}'.format(left, right))
                        return None
            elif t in OPERATORs_DICT_math_U:
                stack_l.append(OPERATORs_DICT_math_U[t](right))
            else:
                stack_l.append(OPERATORs_DICT_func_1[t](right))
        elif t in DICT_VARS:
            stack_l.append(DICT_VARS[t])
        else:
            print('{} was not found in VARs'.format(t))
            return None
    if len(stack_l) != 1:
        print('Error stack ', stack_l)
        return None
    return stack_l[0]






if __name__ == "__main__":

    DICT_VARS = {'R2': 5., 'pi': math.pi}
    expression1 = '2^3 + 3^(1+1)'
    nya2 = tokenize(expression1)
    print('nya22= ', nya2)
    res = tokensPostfixing(nya2)
    solve = postfixTokenCalc(res, DICT_VARS)
    #print('RESULT2 = ', solve)

    print(f'{expression1} = {solve}')
