import { useMutation } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";
import { login as loginApi } from "../api";
import { setToken, setStoredUser } from "@/lib/auth";
import type { LoginRequest } from "../types";

export function useLogin() {
  const navigate = useNavigate();
  return useMutation({
    mutationFn: (data: LoginRequest) => loginApi(data),
    onSuccess: (data) => {
      setToken(data.access_token);
      setStoredUser(data.user);
      navigate("/devices");
    },
  });
}
