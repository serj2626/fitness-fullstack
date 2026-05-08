export interface IField<T> {
  value: T;
  error: string;
  required: boolean;
}
export const useForm = <T extends Record<string, any>>(data: {
  [K in keyof T]: IField<T[K]>;
}) => {
  const { $api } = useNuxtApp();
  const loadingForm = ref(false);
  const errorForm = ref("");

  // reactive сохраняет типы полей
  const formData = reactive(data);

  const submit = async (url: string) => {
    try {
      loadingForm.value = true;
      errorForm.value = "";

      // Собираем только .value, типы "схлопываются" в any для API
      const payload = Object.fromEntries(
        Object.entries(formData).map(([key, field]) => [
          key,
          (field as IField<any>).value,
        ]),
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
    formData, // ← теперь с типами: formData.age.value = number
    submit,
  };
};
