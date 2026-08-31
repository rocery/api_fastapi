import { Table, TableHeader, TableRow, TableHead, TableBody, TableCell } from "@/components/ui/table";
import { formatDate, formatNumber } from "@/utils/format";
import type { IspSpeedtestResponse } from "../types";

export function IspSpeedtestTable({ data }: { data: IspSpeedtestResponse[] }) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>ID</TableHead>
          <TableHead>ISP</TableHead>
          <TableHead>Download</TableHead>
          <TableHead>Upload</TableHead>
          <TableHead>Ping</TableHead>
          <TableHead>Server City</TableHead>
          <TableHead>Server</TableHead>
          <TableHead>Created At</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {data.map((r) => (
          <TableRow key={r.id}>
            <TableCell>{r.id}</TableCell>
            <TableCell className="font-medium">{r.isp}</TableCell>
            <TableCell>{formatNumber(r.download_mbps)} Mbps</TableCell>
            <TableCell>{formatNumber(r.upload_mbps)} Mbps</TableCell>
            <TableCell>{formatNumber(r.ping_ms)} ms</TableCell>
            <TableCell>{r.server_city}</TableCell>
            <TableCell>{r.server ?? "-"}</TableCell>
            <TableCell className="text-xs">{formatDate(r.created_at)}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
