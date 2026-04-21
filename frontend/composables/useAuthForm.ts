import { clearForm } from "~/utils/functions";

export interface IField<T> {
  value: T;
  error: string;
  required: boolean;
}

export const useForm = (data: Record<string, IField<string>>) => {
  const { $api } = useNuxtApp();
  const loading = ref<boolean>(false);
  const errorForm = ref<string>("");
  const formData = reactive(data);

  const validateForm = (data: Record<string, IField<string>>): boolean => {
    let isValid = true;
    Object.keys(data).forEach((key) => {
      const field = data[key];
      if (field.required && !field.value) {
        field.error = "Поле обязательно";
        isValid = false;
      }
    });
    return isValid;
  };

  const submit = async (url: string) => {
    if (!validateForm(formData)) return;

    try {
      loading.value = true;
      errorForm.value = "";

      await $api(url, {
        method: "POST",
        body: formData,
      });

      clearForm(formData);
    } catch (e) {
      errorForm.value = extractError(e) || "Неизвестная ошибка";
    } finally {
      loading.value = false;
    }
  };

  return {
    loading,
    errorForm,
    formData,
    submit,
  };
};
