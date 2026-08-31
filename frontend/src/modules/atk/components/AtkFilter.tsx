import { Input } from "@/components/ui/input";

export function AtkFilter({ value, onChange }: { value: string; onChange: (v: string) => void }) {
  return <Input placeholder="Filter by item or varian..." value={value} onChange={(e) => onChange(e.target.value)} className="max-w-sm" />;
}
