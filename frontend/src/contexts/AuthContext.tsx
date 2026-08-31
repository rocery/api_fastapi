import { createContext, useEffect, useState, useCallback, type ReactNode } from "react";
import { api } from "@/lib/api";
import { getToken, setToken, clearAuth, getStoredUser, setStoredUser } from "@/lib/auth";
import type { User, LoginRequest } from "@/modules/auth/types";

interface AuthContextValue {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (data: LoginRequest) => Promise<void>;
  logout: () => void;
  refreshMe: () => Promise<void>;
}

export const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(getStoredUser());
  const [token, setTokenState] = useState<string | null>(getToken());
  const [isLoading, setIsLoading] = useState<boolean>(!!getToken());

  const refreshMe = useCallback(async () => {
    const t = getToken();
    if (!t) {
      setUser(null);
      setIsLoading(false);
      return;
    }
    try {
      const { data } = await api.get<User>("/auth/me");
      setUser(data);
      setStoredUser(data);
    } catch {
      clearAuth();
      setUser(null);
      setTokenState(null);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    if (token) refreshMe();
    else setIsLoading(false);
  }, [token, refreshMe]);

  const login = async (data: LoginRequest) => {
    const res = await api.post<{ access_token: string; token_type: string; user: User }>("/auth/login", data);
    const { access_token, user: u } = res.data;
    setToken(access_token);
    setStoredUser(u);
    setTokenState(access_token);
    setUser(u);
  };

  const logout = () => {
    clearAuth();
    setUser(null);
    setTokenState(null);
    window.location.href = "/login";
  };

  return (
    <AuthContext.Provider value={{ user, token, isAuthenticated: !!token && !!user, isLoading, login, logout, refreshMe }}>
      {children}
    </AuthContext.Provider>
  );
}
