from PyQt5.QtWidgets import QFileDialog

def save(parent,field):
    save_file = QFileDialog.getSaveFileName(filter='PIE save (*.pie)')[0]
    save_data = saveField(field)
    try:
        with open(save_file, 'w') as file:
            for cell in save_data:
                for el in cell:
                    file.write(str(el) + ';')
                file.write('\n')
    except:
        with open('logs', 'a') as log_file:
            log_file.write('Не создан файл сохранения')

# Сохранение объекта
def saveField(field):
    saveProperty = []
    for col in field:
        for cell in col:
            saveProperty.append([])
            # Основные хар-ки клетки
            saveProperty[-1].append(cell.received_code[0])
            saveProperty[-1].append(cell.received_code[1])
            # Средства обнаружения
            for value in cell.modifies_flags.values():
                saveProperty[-1].append(value)
            
    return(saveProperty)

# Загрузка файла
def load(parent):
    try:
        field = parent.field
        parent.clearPath()
        parent.outputButton.setText('')
        load_file = QFileDialog.getOpenFileName(filter='PIE save (*.pie)')[0]
        with open(load_file, 'r') as file:
            load_file = file.readlines()
        i = 0
        for col in field:
            for cell in col:
                el_t = load_file[i].split(';')[:-1]
                el = []
                for j in el_t:
                    if j=='None':
                        el.append(None)
                    else:
                        el.append(int(j)) 
                # Очищаем поле
                for key in cell.modifies_flags:
                    cell.modifies_flags[key]=0
                cell.cellProcess([0,None])
                
                # Проходимся по модификаторам...
                index = 2
                for key in cell.modifies_flags:
                    if el[index]:
                        cell.modifies_flags[key]=1
                    index += 1
                    if index+1 > len(el):
                        break

                # ... и по основным свойства
                cell.cellProcess([el[0],el[1]])
                i += 1
    except:
        with open('logs', 'a') as log_file:
            log_file.write('Ошибка файла загрузки\n')