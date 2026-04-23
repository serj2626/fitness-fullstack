export interface IField<T> {
  value: T;
  error: string;
  required: boolean;
}

export const useForm = (data: Record<string, IField<string>>) => {
  const { $api } = useNuxtApp();
  const loadingForm = ref(false);
  const errorForm = ref("");

  const formData = reactive(data);

  const submit = async (url: string) => {
    try {
      loadingForm.value = true;
      errorForm.value = "";

      const payload = Object.fromEntries(
        Object.entries(formData).map(([key, field]) => [key, field.value]),
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
    formData,
    submit,
  };
};
