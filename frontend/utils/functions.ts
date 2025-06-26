interface FormField {
  value: string | boolean;
  error: string;
  required: boolean;
}

interface FormData {
  [key: string]: FormField;
}

export const clearFormAuth = (formData: FormData) => {
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
  return [useRuntimeConfig().public.media_url, videoUrl].join("");
};

export const getMedia = (mediaContentUrl: string) => {
  return [useRuntimeConfig().public.media_url, mediaContentUrl].join("");
};

export const formatNumber = (num: number): string => {
  return num.toLocaleString("ru-RU");
};

export const formatNumberCustom = (num: number, separator = " "): string => {
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, separator);
};

export const goNextPage = (path: string) => {
  return window.open(path, "_blank");
};

export const formatDate = (date: string) => {
  return new Date(date).toLocaleDateString("ru-RU", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
};
