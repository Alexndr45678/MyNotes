class View(object):
    @staticmethod
    def show_number_point_list(notes):
        for note in notes:
            print(note)

    @staticmethod
    def show_note(note):
        print(note)

    @staticmethod
    def show_empty_list_message():
        print('Cписок заметок пустой.')

    @staticmethod
    def display_note_id_not_exist(note_id):
        print('Заметка №{} не найдена.'.format(note_id))

    @staticmethod
    def display_note_id_exist(note_id):
        print('Заметка №{} уже есть.'.format(note_id))

    @staticmethod
    def display_note_stored():
        print('Заметка успешно добавлена.')

    @staticmethod
    def display_note_updated(note_id):
        print('Заметка №{} обновлена.'.format(note_id))

    @staticmethod
    def display_note_deletion(note_id):
        print('Заметка №{} удалена.'.format(note_id))

    @staticmethod
    def display_all_notes_deletion():
        print('Все заметки удалены!')

def display_note_id_not_exist(search_id):
    return search_id