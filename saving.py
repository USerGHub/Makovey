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
            # Средства обнаружения
            for value in cell.modifies_flags.values():
                saveProperty[-1].append(value)
            # Основные хар-ки клетки
            saveProperty[-1].append(cell.received_code[0])
            saveProperty[-1].append(cell.received_code[1])
            
    return(saveProperty)

# Загрузка файла
def load(parent):
    try:
        field = parent.field
        parent.clearPath()
        parent.outputLabel.setText('')
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
                cell.cellProcess([0,None,None])
                # Проходимся по модификаторам...
                for index in range(len(el)-2):
                    if el[index]:
                        cell.cellProcess([None,None,index+1])
                # ... и по основным свойства
                if el[-2]:
                    cell.cellProcess([el[-2],el[-1],None])
                i += 1
    except:
        with open('logs', 'a') as log_file:
            log_file.write('Ошибка файла загрузки')