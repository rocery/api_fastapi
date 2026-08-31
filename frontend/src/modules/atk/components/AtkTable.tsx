import { Table, TableHeader, TableRow, TableHead, TableBody, TableCell } from "@/components/ui/table";
import { formatCurrency } from "@/utils/format";
import type { AtkResponse } from "../types";

export function AtkTable({ data }: { data: AtkResponse[] }) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>ID</TableHead>
          <TableHead>Varian</TableHead>
          <TableHead>Item</TableHead>
          <TableHead>Satuan</TableHead>
          <TableHead className="text-right">Harga</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {data.map((r) => (
          <TableRow key={r.id}>
            <TableCell>{r.id}</TableCell>
            <TableCell>{r.varian ?? "-"}</TableCell>
            <TableCell>{r.item ?? "-"}</TableCell>
            <TableCell>{r.satuan ?? "-"}</TableCell>
            <TableCell className="text-right">{r.harga != null ? formatCurrency(r.harga) : "-"}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
