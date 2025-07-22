interface FormField {
  value: string | boolean;
  error: string;
  required: boolean;
}

interface FormData {
  [key: string]: FormField;
}

export const clearFormAuth = (formData: FormData) => {
  // Функция для очистки формы

  for (const key in formData) {
    if (key === "remember") {
      formData[key].value = false;
      formData[key].error = "";
    } else {
      formData[key].value = "";
      formData[key].error = "";
    }
  }
};

export const getVideo = (videoUrl: string | undefined) => {
  // Функция для получения URL-адреса видео

  return [useRuntimeConfig().public.media_url, videoUrl].join("");
};

export const getMedia = (mediaContentUrl: string) => {
  // Функция для получения URL-адреса медиа-контента

  return [useRuntimeConfig().public.media_url, mediaContentUrl].join("");
};

export const formatNumber = (num: number): string => {
  // Функция для форматирования числа

  return num.toLocaleString("ru-RU");
};

export const formatNumberCustom = (num: number, separator = " "): string => {
  // Функция для форматирования числа

  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, separator);
};

export const goNextPage = (path: string) => {
  // Функция для перехода на следующую страницу

  return window.open(path, "_blank");
};

export const formatDate = (date: string) => {
  // Функция для форматирования даты

  return new Date(date).toLocaleDateString("ru-RU", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
};

export const extractError = (err: unknown): string => {
  // Функция для извлечения сообщения об ошибке

  if (err instanceof Error) return err.message;
  if (typeof err === "string") return err;
  return "Неизвестная ошибка";
};

export const getExperience = (count: number): string => {
  // Функция для получения стажа
  if (count === 0) return "не указан";
  if (count === 1) return "более года";
  return `более ${count} лет`;
};