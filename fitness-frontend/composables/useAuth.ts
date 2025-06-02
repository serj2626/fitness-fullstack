export const useAuthApi = () => {
  const config = useRuntimeConfig();

  const register = async (data: {
    phone: string;
    email: string;
    password: string;
    password2: string;
  }) => {
    return await $fetch(`${config.public.apiBase}/api/register/`, {
      method: "POST",
      body: data,
    });
  };

  return { register };
};
