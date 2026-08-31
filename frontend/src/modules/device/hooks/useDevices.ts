import { useQuery } from "@tanstack/react-query";
import { listDevices } from "../api";

export function useDevices() {
  return useQuery({ queryKey: ["devices"], queryFn: listDevices });
}
