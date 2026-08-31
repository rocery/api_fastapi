import { api } from "@/lib/api";
import type { AtkResponse } from "./types";

export async function listAtk(): Promise<AtkResponse[]> {
  const res = await api.get<AtkResponse[]>("/atk");
  return res.data;
}
