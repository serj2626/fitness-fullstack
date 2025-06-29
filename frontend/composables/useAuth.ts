import { api } from "~/api";
const { $api } = useNuxtApp();

export const useVerifyToken = async (token: string) => {
  const response = await $api<{ success: boolean }>(api.users.verify, {
    method: "POST",
    body: { token },
  });
  return response.success;
};
