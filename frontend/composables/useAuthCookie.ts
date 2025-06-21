export const useAuthCookie = () => {
  const cookie = useCookie("secure_token", {
    httpOnly: true, // Защита от XSS
    secure: process.env.NODE_ENV === "production", // Только HTTPS
    sameSite: "strict", // Защита от CSRF
    maxAge: 60 * 15, // 15 минут для критичных данных
  });
  const setToken = (token: string) => {
    cookie.value = token;
  };

  const getToken = () => {
    return cookie.value;
  };

  return { setToken, getToken };
};
