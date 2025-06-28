import type { H3Event } from "h3";

export function setServerTokens(event: H3Event, access: string, refresh: string) {
  setCookie(event, "access_token", access, {
    httpOnly: true,
    secure: true,
    sameSite: "strict",
    maxAge: 60 * 5,
    path: "/",
  });

  setCookie(event, "refresh_token", refresh, {
    httpOnly: true,
    secure: true,
    sameSite: "strict",
    maxAge: 60 * 60 * 24 * 7,
    path: "/",
  });
}
