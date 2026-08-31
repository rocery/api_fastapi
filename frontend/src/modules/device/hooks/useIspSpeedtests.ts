import { useQuery } from "@tanstack/react-query";
import { listIspSpeedtests } from "../api";
import type { IspSpeedtestParams } from "../types";

export function useIspSpeedtests(params: IspSpeedtestParams) {
  return useQuery({
    queryKey: ["isp_speedtests", params],
    queryFn: () => listIspSpeedtests(params),
  });
}
