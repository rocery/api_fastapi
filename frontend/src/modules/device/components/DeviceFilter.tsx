import { Input } from "@/components/ui/input";

export function DeviceFilter({ value, onChange }: { value: string; onChange: (v: string) => void }) {
  return <Input placeholder="Filter by name, IP, or location..." value={value} onChange={(e) => onChange(e.target.value)} className="max-w-sm" />;
}
