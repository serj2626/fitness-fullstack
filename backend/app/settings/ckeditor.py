# 2. Подключаем наше кастомное хранилище для CKEditor
CKEDITOR_5_FILE_STORAGE = "app.storage.CKEditor5Storage"


CKEDITOR_5_CUSTOM_COLOR_PALETTE = [
    {"color": "hsl(4, 90%, 58%)", "label": "Красный"},
    {"color": "hsl(340, 82%, 52%)", "label": "Розовый"},
    {"color": "hsl(291, 64%, 42%)", "label": "Фиолетовый"},
    {"color": "hsl(262, 52%, 47%)", "label": "Темно-фиолетовый"},
    {"color": "hsl(231, 48%, 48%)", "label": "Индиго"},
    {"color": "hsl(207, 90%, 54%)", "label": "Синий"},
    {"color": "hsl(100, 60%, 50%)", "label": "Зеленый"},
    {"color": "hsl(45, 100%, 50%)", "label": "Желтый"},
    {"color": "hsl(0, 0%, 0%)", "label": "Черный"},
    {"color": "hsl(0, 0%, 100%)", "label": "Белый"},
]

# 2. Основной конфиг для расширенного редактора
CKEDITOR_5_CONFIGS = {
    "extends": {
        # Блок с инструментами над редактором (быстрый доступ к стилям)
        "blockToolbar": [
            "paragraph",
            "heading1",
            "heading2",
            "heading3",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "blockQuote",
        ],
        # Основная панель инструментов (всё, что нужно для постов)
        "toolbar": [
            # Стили заголовков
            "heading",
            "|",
            # Отступы
            "outdent",
            "indent",
            "|",
            # Форматирование текста
            "bold",
            "italic",
            "link",
            "underline",
            "strikethrough",
            "code",
            "subscript",
            "superscript",
            "|",
            # Выравнивание (то, что ты просил!)
            "alignment",  # добавил выравнивание [citation:8]
            "|",
            # Выделение и блоки
            "highlight",
            "codeBlock",
            "sourceEditing",
            "|",
            # Медиа и списки
            "insertImage",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "blockQuote",
            "imageUpload",
            "mediaEmbed",
            "removeFormat",
            "|",
            # Размеры и цвета текста
            "fontSize",
            "fontFamily",
            "fontColor",
            "fontBackgroundColor",
            "|",
            # Таблицы
            "insertTable",
        ],
        # === Настройки изображений ===
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
                "imageStyle:alignLeft",  # выравнивание картинки влево
                "imageStyle:alignCenter",  # по центру
                "imageStyle:alignRight",  # вправо
                "imageStyle:side",  # сбоку (обтекание текстом)
                "|",
            ],
            "styles": [
                "full",  # на всю ширину
                "side",  # сбоку
                "alignLeft",  # слева
                "alignRight",  # справа
                "alignCenter",  # по центру
            ],
        },
        # === Настройки таблиц (с цветами) ===
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableProperties",
                "tableCellProperties",
            ],
            "tableProperties": {
                "borderColors": CKEDITOR_5_CUSTOM_COLOR_PALETTE,
                "backgroundColors": CKEDITOR_5_CUSTOM_COLOR_PALETTE,
            },
            "tableCellProperties": {
                "borderColors": CKEDITOR_5_CUSTOM_COLOR_PALETTE,
                "backgroundColors": CKEDITOR_5_CUSTOM_COLOR_PALETTE,
            },
        },
        # === Настройки заголовков ===
        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Обычный текст",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Заголовок 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Заголовок 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Заголовок 3",
                    "class": "ck-heading_heading3",
                },
                {
                    "model": "heading4",
                    "view": "h4",
                    "title": "Заголовок 4",
                    "class": "ck-heading_heading4",
                },
            ]
        },
        # === Настройки списков ===
        "list": {
            "properties": {
                "styles": True,
                "startIndex": True,
                "reversed": True,
            }
        },
        # === Язык ===
        "language": "ru",  # можно явно указать русский [citation:7]
        # === Плагины и прочее ===
        "removePlugins": ["MediaEmbedToolbar"],  # убираем лишнее (если надо)
    },
}

# 3. (Опционально) Автоматический выбор языка из Django
CKEDITOR_5_USER_LANGUAGE = (
    True  # если True, язык подтянется из текущей сессии пользователя [citation:4]
)

# 4. Ограничения на загрузку файлов
CKEDITOR_5_MAX_FILE_SIZE = 2  # Максимальный размер файла в MB [citation:4]
CKEDITOR_5_ALLOW_ALL_FILE_TYPES = False  # Разрешать только картинки
CKEDITOR_5_UPLOAD_FILE_TYPES = [
    "jpeg",
    "jpg",
    "png",
    "gif",
    "webp",
]  # список допустимых типов
