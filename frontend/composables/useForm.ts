export interface IField<T> {
  value: T;
  error: string;
  required: boolean;
}

// 🔥 Generic-версия: T — это точная форма { name: IField<string>, agree: IField<boolean>, ... }
export const useForm = <T extends Record<string, IField<any>>>(data: T) => {
  const { $api } = useNuxtApp();
  const loadingForm = ref(false);
  const errorForm = ref("");
  
  // 🔥 reactive сохраняет точные типы полей
  const formData = reactive(data) as { [K in keyof T]: IField<T[K]['value']> };

  const validateForm = (): boolean => {
    let isValid = true;
    Object.keys(formData).forEach((key) => {
      const field = formData[key as keyof typeof formData];
      if (field.required && !field.value) {
        field.error = "Поле обязательно";
        isValid = false;
      }
    });
    return isValid;
  };

  const submit = async (url: string) => {
    if (!validateForm()) return;
    try {
      loadingForm.value = true;
      errorForm.value = "";
      
      // 🔥 Собираем только значения для отправки
      const payload = Object.fromEntries(
        Object.entries(formData).map(([key, field]) => [key, field.value])
      );
      
      await $api(url, { method: "POST", body: payload });
      clearForm(formData);
    } catch (e) {
      errorForm.value = extractError(e) || "Неизвестная ошибка";
    } finally {
      loadingForm.value = false;
    }
  };

  return {
    loadingForm,
    errorForm,
    formData, // 🔥 Теперь имеет точные типы!
    submit,
  };
};