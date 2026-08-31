import { useQuery } from "@tanstack/react-query";
import { fetchMe } from "../api";
import { getToken } from "@/lib/auth";

export function useMe() {
  return useQuery({
    queryKey: ["me"],
    queryFn: fetchMe,
    enabled: !!getToken(),
  });
}
