import { useState, useMemo } from "react";
import { useAtk } from "../hooks/useAtk";
import { AtkTable } from "../components/AtkTable";
import { AtkFilter } from "../components/AtkFilter";
import { Loading } from "@/components/feedback/Loading";
import { ErrorAlert } from "@/components/feedback/ErrorAlert";
import { EmptyState } from "@/components/feedback/EmptyState";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";

export function AtkListPage() {
  const { data, isLoading, error } = useAtk();
  const [filter, setFilter] = useState("");

  const filtered = useMemo(() => {
    if (!data) return [];
    if (!filter) return data;
    const q = filter.toLowerCase();
    return data.filter((r) => [r.item, r.varian].some((v) => v?.toLowerCase().includes(q)));
  }, [data, filter]);

  if (isLoading) return <Loading />;
  if (error) return <ErrorAlert message={(error as Error).message} />;

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">ATK</h1>
      <Card>
        <CardHeader>
          <CardTitle>ATK List</CardTitle>
          <AtkFilter value={filter} onChange={setFilter} />
        </CardHeader>
        <CardContent>
          {filtered.length === 0 ? <EmptyState message="No ATK records." /> : <AtkTable data={filtered} />}
        </CardContent>
      </Card>
    </div>
  );
}
