import random as r
import string as s


def build_random_dic():
    rnd_dict_list = [{r.choice(s.ascii_lowercase): r.randrange(0, 99) for j in range(r.randrange(0, 25))} for i in
                     range(r.randrange(1, 9))]
    return rnd_dict_list


def build_common_dic(rnd_dic_list):
    common_dic = {}
    cnt_iter = 0
    cnt_rep = 1
    for dct in rnd_dic_list:
        for key, value in dct.items():
            if key in common_dic:
                if value > common_dic[key][0]:
                    common_dic[key] = [value, cnt_iter, cnt_rep + 1]
                else:
                    common_dic[key][2] = cnt_rep + 1
            else:
                cnt_rep = 1
                common_dic[key] = [value, cnt_iter, cnt_rep]
        cnt_iter += 1
    return common_dic


def build_final_dic(common_dict):
    dict_final = {}
    for key, (value, cnt, cnt_rep) in common_dict.items():
        if cnt_rep == 1:
            dict_final[key] = value
        else:
            dict_final[f'{key}_{cnt}'] = value
    return dict_final


original_dic = build_random_dic()
compr_dict = build_common_dic(original_dic)
print(build_final_dic(compr_dict))