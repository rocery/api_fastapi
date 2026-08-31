import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";

interface Props {
  server: string;
  period: string;
  onServerChange: (v: string) => void;
  onPeriodChange: (v: string) => void;
  onReset: () => void;
}

export function IspSpeedtestFilter({ server, period, onServerChange, onPeriodChange, onReset }: Props) {
  return (
    <div className="flex flex-wrap items-end gap-4">
      <div className="space-y-1">
        <Label htmlFor="server">Server</Label>
        <Input id="server" placeholder="e.g. jakarta" value={server} onChange={(e) => onServerChange(e.target.value)} className="w-48" />
      </div>
      <div className="space-y-1">
        <Label htmlFor="period">Period (YYYY-MM)</Label>
        <Input id="period" placeholder="2026-01" value={period} onChange={(e) => onPeriodChange(e.target.value)} pattern="^\d{4}-(0[1-9]|1[0-2])$" className="w-40" />
      </div>
      <Button variant="outline" onClick={onReset}>Reset</Button>
    </div>
  );
}
