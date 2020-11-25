def score_errors(self, prediction, y):
    first_all = 0
    first_false = 0
    first_acc = 0
    first_max_acc = 0
    second_all = 0
    second_false = 0
    second_acc = 0
    second_max_acc = 0
    second_hd_avg = 0
    second_hd_max = 0
    second_hd_min = 1
    for i in range(len(prediction)):
        # d = np.less(np.abs(np.array(y[i]) - np.array(prediction[i])), [settings.MODUL / 2]*len(settings.KEY_l)).astype('int')
        # s = np.sum(d)
        s = self.Hemming_distance(np.array(y[i]), np.array(prediction[i]))
        
        acc = (1 - s/len(settings.KEY_l))
        if (y[i] == np.array(settings.KEY_l)).all():
            first_all += 1
            first_acc += acc
            if acc > first_max_acc:
                first_max_acc = acc
            if s > 0:
                first_false += 1
        else:
            second_all += 1
            second_acc += acc
            if acc > second_max_acc:
                second_max_acc = acc
            
            d = self.Hemming_distance(np.array(prediction[i]), np.array(settings.KEY_l))/len(settings.KEY_l)
            second_hd_avg += d
            if d > second_hd_max:
                second_hd_max = d
            if d < second_hd_min:
                second_hd_min = d
            if d == 0:
                second_false += 1

    first_error = first_false / first_all
    second_error = second_false / second_all
    first_acc_avg = first_acc / first_all
    second_acc_avg = second_acc / second_all
    second_hd_avg = second_hd_avg / second_all

    print("Количество тестовых данных = ", len(prediction))
    print('Полное количество "своих" = {a:d}, количество ложных срабатываний = {f:d}, отношение ложных срабатываний к всем "своим" = {e:.5f}, средняя точность = {a_a:.5f}, max_acc = {m_a:.5f}'.format(a = first_all, f = first_false, e=first_error, a_a=first_acc_avg, m_a=first_max_acc))
    print('Полное количество "чужих" = {a:d}, количество ложных пропусков = {f:d}, отношение ложных пропусков ко всем "чужим" = {e:.5f}, среднее расстояние Хемминга = {hd_a:.5f}, max расстояние Хемминга = {hd_max:.5f}, min расстояние Хемминга = {hd_min:.5f}'.format(a=second_all, f=second_false, e=second_error, hd_a=second_hd_avg, hd_max=second_hd_max, hd_min=second_hd_min))
