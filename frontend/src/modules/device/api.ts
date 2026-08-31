import { api } from "@/lib/api";
import type { DeviceResponse, IspSpeedtestResponse, IspSpeedtestParams } from "./types";

export async function listDevices(): Promise<DeviceResponse[]> {
  const res = await api.get<DeviceResponse[]>("/devices/list");
  return res.data;
}

export async function listIspSpeedtests(params: IspSpeedtestParams = {}): Promise<IspSpeedtestResponse[]> {
  const res = await api.get<IspSpeedtestResponse[]>("/devices/isp_speedtest", { params });
  return res.data;
}
