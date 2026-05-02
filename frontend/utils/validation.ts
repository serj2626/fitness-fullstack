import type { IOrderItems } from "~/types";

export const phoneUtils = {
  validate(event) {
    const caretPosition = this.getCaretPosition(event);
    const value = this.getPhoneValue(event);
    event.target.value = this.formatedPhoneInput(value);
    this.setCaretPosition(event, caretPosition);
  },

  getCaretPosition(event): number {
    const position = event.target.selectionStart;
    const isDeleting =
      event.inputType === "deleteContentBackward" ||
      event.inputType === "deleteContentForward";

    if (position < 4) {
      return isDeleting ? 3 : 4;
    }
    if (position > 6 && position < 8) {
      return isDeleting ? 6 : 8;
    }
    if (position === 11) {
      return isDeleting ? 10 : 12;
    }
    if (position === 14) {
      return isDeleting ? 13 : 15;
    }
    return position;
  },
  getPhoneValue(event) {
    if (event.target.value.length === 11 && event.target.value[0] === "8") {
      event.target.value = event.target.value.slice(1);
    }

    let value = event.target.value.replace(/(\+7)|\D/g, "");

    if (value.length >= 10) {
      event.target.value = event.target.value.slice(0, 17);
      value = value.slice(0, 10);
    }

    return value;
  },
  formatedPhoneInput(value: string) {
    if (value.startsWith("7") || value.startsWith("8")) {
      value = "";
      return "+7 ";
    }

    const match = value.match(/^(\d{1,3})(\d{0,3})(\d{0,2})(\d{0,2})$/);
    if (match) {
      return `+7 ${match[1]}${match[2] ? " " : ""}${match[2]}${
        match[3] ? " " : ""
      }${match[3]}${match[4] ? " " : ""}${match[4]}`;
    } else {
      return "";
    }
  },
  setCaretPosition(event, position: number) {
    event.target.selectionStart = position;
    event.target.selectionEnd = position;
  },
};

export const validateCredentials = (
  currentRuleset: {
    minLength: { condition: number; message: string };
    maxLength: { condition: number; message: string };
    // pattern: { condition: RegExp; message: string };
  },
  value: string,
) => {
  switch (true) {
    case String(value).length < currentRuleset.minLength.condition:
      return currentRuleset.minLength.message;

    case String(value).length > currentRuleset.maxLength.condition:
      return currentRuleset.maxLength.message;

    case !String(value).match(currentRuleset.pattern.condition):
      return currentRuleset.pattern.message;

    default:
      return "";
  }
};

export const validateFullName = (value: string) =>
  validateCredentials(
    {
      minLength: {
        condition: 2,
        message: "Минимальная длина - 2 символа",
      },
      maxLength: {
        condition: 100,
        message: "Максимальная длина - 100 символов",
      },
      // pattern: {
      //   condition: /^[а-я А-ЯёЁ-]+$/,
      //   message: 'Поле может содержать только русские буквы или "-"',
      // },
    },
    value,
  );

export const validateProductID = (value: string) => {
  if (!value) {
    return "Товар не выбран";
  }
  return "";
};

export const validateFiles = (value: File[] | null) => {
  if (!value || !value.length) {
    return "Необходимо прикрепить файл с реквизитами";
  }

  const file = value[0];
  const maxSizeMB = 10;
  const allowedTypes = [
    "application/pdf",
    "image/jpeg",
    "image/png",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
  ];

  if (!allowedTypes.includes(file.type)) {
    return "Допустимые форматы файлов: PDF, JPG, PNG, DOC, DOCX";
  }

  if (file.size > maxSizeMB * 1024 * 1024) {
    return `Максимальный размер файла — ${maxSizeMB} МБ`;
  }

  return "";
};

export const validateItems = (value: IOrderItems[]) => {
  if (!value || !value.length) {
    return "Корзина пуста. Добавьте хотя бы один товар";
  }

  for (const item of value) {
    if (!item.product_id) {
      return "Некорректный товар в корзине";
    }
    if (!item.quantity || item.quantity <= 0) {
      return "Количество товара должно быть больше нуля";
    }
  }

  return "";
};

export const validateComment = (value: string) => {
  const maxLength = {
    condition: 600,
    message: "Максимальная длина - 600 символов",
  };
  const pattern = {
    condition: /^[\wа-яА-ЯёЁ\d.,?!:;()%№@+="\s-]+$/,
    message:
      'Поле может содержать только русские/латинские буквы и символы "-.,?!-:;()%№@+="',
  };

  switch (true) {
    case String(value).length === 0:
      return "Поле не может быть пустым";
    case String(value).length > maxLength.condition:
      return maxLength.message;

    case !String(value).match(pattern.condition):
      return pattern.message;

    default:
      return "";
  }
};

export const validatePhoneNumber = (value: string | number) => {
  value = String(value).replace(/[^0-9]/g, "");

  const length = {
    condition: 11,
    message: "Некорректно введен номер телефона",
  };

  if (String(value).length === 0) {
    return "Поле обязательно для заполнения";
  }

  if (String(value).length !== length.condition) {
    return length.message;
  }

  return "";
};

export const validateEmail = (value: string) =>
  validateCredentials(
    {
      minLength: {
        condition: 2,
        message: "Минимальная длина - 2 символа",
      },
      maxLength: {
        condition: 100,
        message: "Максимальная длина - 100 символов",
      },
      pattern: {
        condition: /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/,
        message: "Введите корректный email",
      },
    },
    value,
  );

export const validateServiceId = (value: number) => {
  if (isNaN(value)) {
    return "Выберите услугу";
  }

  return "";
};

export const validateAgree = (value: boolean) => {
  if (!value) {
    return "Вы должны согласиться с условиями";
  }

  return "";
};

export type TFormData = {
  [key: string]: {
    value: string | number | File[] | null | boolean;
    error: string;
    required: boolean;
  };
};

export const checkForm = (formData: TFormData): boolean => {
  let error = false;

  for (const key in formData) {
    if (formData[key].required) {
      if (key === "agree") {
        formData[key].error = validateAgree(formData[key].value);
        if (formData[key].error) {
          error = true;
        }
      }
      if (key === "phone") {
        formData[key].error = validatePhoneNumber(formData[key].value);
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "email") {
        formData[key].error = validateEmail(String(formData[key].value));
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "service") {
        formData[key].error = validateServiceId(Number(formData[key].value));
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "name") {
        formData[key].error = validateFullName(String(formData[key].value));
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "product") {
        formData[key].error = validateProductID(String(formData[key].value));
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "captcha") {
        formData[key].error = formData[key].value
          ? ""
          : "Необходимо пройти антиспам проверку";
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "message") {
        formData[key].error = validateComment(String(formData[key].value));
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "files") {
        formData[key].error = validateFiles(formData[key].value);
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "items") {
        formData[key].error = validateItems(formData[key].value);
        if (formData[key].error) {
          error = true;
        }
      }
    }
  }
  return error;
};
