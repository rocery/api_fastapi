// Simple Zustand-like store without zustand dependency — uses localStorage directly.
// If you prefer zustand: npm install zustand and replace with create().
import { getToken, setToken, clearAuth, getStoredUser, setStoredUser } from "@/lib/auth";
import type { User } from "@/modules/auth/types";

type Listener = () => void;
const listeners = new Set<Listener>();

function notify() {
  listeners.forEach((l) => l());
}

export const authStore = {
  getToken,
  setToken: (t: string) => {
    setToken(t);
    notify();
  },
  clearAuth: () => {
    clearAuth();
    notify();
  },
  getUser: getStoredUser,
  setUser: (u: User) => {
    setStoredUser(u);
    notify();
  },
  subscribe: (l: Listener) => {
    listeners.add(l);
    return () => listeners.delete(l);
  },
};
