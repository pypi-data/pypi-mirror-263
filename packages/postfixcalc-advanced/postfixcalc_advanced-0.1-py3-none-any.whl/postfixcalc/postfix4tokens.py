from postfixcalc_advanced.exp_tokenization import tokenize#, tokenize
from postfixcalc_advanced.avaliable_math_logic_operators import OPERATORs_DICT_func_1, OPERATORs_PRECEDENCE_DICT, \
    OPERATORs_DICT_binary_between, OPERATORs_DICT_math_U, OPERATORs_DICT_func_2
from postfixcalc_advanced.avaliable_math_logic_operators import before_unar_arithmetic


def tokensPostfixing(tokens: list, brackets=None):
    """
    new vars
    :param tokens:
    :param brackets: brackets[0] - open bracket, brackets[1] - close bracket
    :return:
    """
    if brackets is None:
        brackets = ['(', ')', '[', ']']
    stack = []
    result = []
    start_exp = True
    for t in tokens:
        try:
            t = float(t)
            result.append(t)
        except:
            if t in OPERATORs_DICT_func_1 or t in OPERATORs_DICT_func_2:#sin, int, pow
                stack.append(t)
            elif t ==',':
                while stack[-1] != brackets[0]:
                    result.append(stack.pop(-1))
                    if len(stack) == 0:
                        print('wrong expression: "{}" is missing'.format(brackets[0]))
                        return None
            elif t in OPERATORs_DICT_binary_between:
                t = '_' if (t == '-' and start_exp) else t
                while len(stack) > 0 and (stack[-1] in OPERATORs_DICT_binary_between or stack[-1] in OPERATORs_DICT_math_U) and OPERATORs_PRECEDENCE_DICT[stack[-1]] >= OPERATORs_PRECEDENCE_DICT[t]:
                    result.append(stack.pop(-1))
                if not(t == '+' and start_exp):
                    stack.append(t)
            elif t == brackets[0]:
                stack.append(t)
            elif t == brackets[1]:
                while len(stack) > 0 and stack[-1] != brackets[0]:
                    result.append(stack.pop(-1))
                if len(stack) == 0 or stack[-1] != brackets[0]:
                    return None
                stack.pop(-1)
                if len(stack) > 0 and (stack[-1] in OPERATORs_DICT_func_1 or stack[-1] in OPERATORs_DICT_func_2):
                    result.append(stack.pop(-1))
            else:
                result.append(t)
        if t in before_unar_arithmetic:
            start_exp = True
        else:
            start_exp = False

    while len(stack) > 0:
        if stack[-1] == brackets[0]:
            print('Not enough brackets')
            return None
        result.append(stack.pop(-1))
    result = tuple(result)
    return result



def string2postfix_tuple(infix:str, brackets):#, vars:dict
    print(f'string2postfix_tuple : ', str)
    infix_list = tokenize(infix, brackets)
    print('infix_list = ', infix_list)
    res = tokensPostfixing(infix_list, brackets)#,vars
    print('string2postfix_tuple res = ', res)
    return res



def test_postfix(infix:str):
    infix_list = tokenize(infix)
    print('infix list = ', infix_list)
    res = tokensPostfixing(infix_list)
    print('res = ', res)
    one_line = ' '.join(map(str, res))
    print('one line', one_line)
    return res





if __name__ == "__main__":
    nya = '(sin(6) + 30)+17 -(-pow(3)+1)'
    nya = '5 + 1==6'
    test_postfix(nya)
