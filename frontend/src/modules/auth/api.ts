import { api } from "@/lib/api";
import type { LoginRequest, LoginResponse, User } from "./types";

export async function login(data: LoginRequest): Promise<LoginResponse> {
  const res = await api.post<LoginResponse>("/auth/login", data);
  return res.data;
}

export async function fetchMe(): Promise<User> {
  const res = await api.get<User>("/auth/me");
  return res.data;
}
