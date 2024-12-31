import pandas as pd

def change_df(df, index, index_condense):
    df['sales'] = pd.to_numeric(df['sales'],errors='coerce')
    df['kEA'] = pd.to_numeric(df['kEA'],errors='coerce')
    df['ton'] = pd.to_numeric(df['ton'],errors='coerce')
    pdf1 = df.pivot_table('sales',index=index,columns='mm',aggfunc='sum',margins=True,margins_name='총계').round(0)
    pdf1_EA = df.pivot_table('kEA',index=index,columns='mm',aggfunc='sum',margins=True,margins_name='총계').round(0)
    pdf1_ton = df.pivot_table('ton',index=index,columns='mm',aggfunc='sum',margins=True,margins_name='총계').round(0)
    pdf1_WP = pdf1/pdf1_ton*1000
    pdf1 = pdf1.reset_index()
    pdf1_EA = pdf1_EA.reset_index()
    pdf1_WP = pdf1_WP.reset_index()
    pdf1 = pdf1.set_index(keys=index_condense,drop=True)
    pdf1_EA = pdf1_EA.set_index(keys=index_condense,drop=True)
    pdf1_WP = pdf1_WP.set_index(keys=index_condense,drop=True)

    for rem in index_condense:
        try:
            index.remove(rem)
        except:
            pass
    pdf1 = pdf1.drop(columns=index, errors='ignore')
    pdf1_EA = pdf1_EA.drop(columns=index, errors='ignore')
    pdf1_WP = pdf1_WP.drop(columns=index, errors='ignore')
    final_pdf = [pdf1,pdf1_EA,pdf1_WP]
    return final_pdf


def overview_sales(var_pre, var_plan, var_now, last_month, previous_month):
    var_return = []
    for i in range(3):
        var_ele = []
        show_list = pd.DataFrame([var_pre[i][last_month],var_plan[i][last_month],var_now[i][previous_month],var_now[i][last_month]],
                                    index=['전년(A)','계획(P)','전월(A)','실적(A)']).T
        show_list['전월比'] = show_list['실적(A)'] - show_list['전월(A)']
        show_list['계획比'] = show_list['실적(A)'] - show_list['계획(P)']
        show_list['동기比'] = show_list['실적(A)'] - show_list['전년(A)']
        show_list_tot = pd.DataFrame([var_pre[i]['총계'],var_plan[i]['총계'],var_now[i]['총계']],
                                    index=['동기누계','누계계획','누계실적']).T
        show_list_tot['누계계획比'] = show_list_tot['누계실적'] - show_list_tot['누계계획']
        show_list_tot['누계동기比'] = show_list_tot['누계실적'] - show_list_tot['동기누계']
        idx1 = list(show_list.index)
        idx1[len(list(idx1))-1] = '계'
        show_list.index = idx1
        show_list_tot.index = idx1
        var_ele.append(show_list)
        var_ele.append(show_list_tot)
        var_return.append(var_ele)
    return var_return
    