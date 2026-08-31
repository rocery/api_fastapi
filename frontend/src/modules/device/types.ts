export interface DeviceResponse {
  device_id: string;
  device_name: string;
  ip_address: string;
  location: string;
  etc: string;
  ping: string | null;
}

export interface IspSpeedtestResponse {
  id: number;
  isp: string;
  download_mbps: number;
  upload_mbps: number;
  ping_ms: number;
  created_at: string;
  server_city: string;
  server: string | null;
}

export interface IspSpeedtestParams {
  server?: string;
  period?: string; // YYYY-MM
}
