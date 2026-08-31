import { Table, TableHeader, TableRow, TableHead, TableBody, TableCell } from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";
import type { DeviceResponse } from "../types";

export function DeviceTable({ devices }: { devices: DeviceResponse[] }) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Device ID</TableHead>
          <TableHead>Name</TableHead>
          <TableHead>IP Address</TableHead>
          <TableHead>Location</TableHead>
          <TableHead>Ping</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {devices.map((d) => (
          <TableRow key={d.device_id}>
            <TableCell className="font-mono text-xs">{d.device_id}</TableCell>
            <TableCell className="font-medium">{d.device_name}</TableCell>
            <TableCell className="font-mono text-xs">{d.ip_address}</TableCell>
            <TableCell>{d.location}</TableCell>
            <TableCell>
              {d.ping ? <Badge variant={Number(d.ping) < 100 ? "default" : "destructive"}>{d.ping} ms</Badge> : <span className="text-muted-foreground">-</span>}
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
