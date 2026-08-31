import { useQuery } from "@tanstack/react-query";
import { listAtk } from "../api";

export function useAtk() {
  return useQuery({ queryKey: ["atk"], queryFn: listAtk });
}
