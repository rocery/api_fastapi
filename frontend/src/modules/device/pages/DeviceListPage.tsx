import { useState, useMemo } from "react";
import { useDevices } from "../hooks/useDevices";
import { DeviceTable } from "../components/DeviceTable";
import { DeviceFilter } from "../components/DeviceFilter";
import { Loading } from "@/components/feedback/Loading";
import { ErrorAlert } from "@/components/feedback/ErrorAlert";
import { EmptyState } from "@/components/feedback/EmptyState";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";

export function DeviceListPage() {
  const { data, isLoading, error } = useDevices();
  const [filter, setFilter] = useState("");

  const filtered = useMemo(() => {
    if (!data) return [];
    if (!filter) return data;
    const q = filter.toLowerCase();
    return data.filter((d) => [d.device_name, d.ip_address, d.location, d.device_id].some((v) => v.toLowerCase().includes(q)));
  }, [data, filter]);

  if (isLoading) return <Loading />;
  if (error) return <ErrorAlert message={(error as Error).message} />;

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Devices</h1>
      <Card>
        <CardHeader>
          <CardTitle>Device List</CardTitle>
          <DeviceFilter value={filter} onChange={setFilter} />
        </CardHeader>
        <CardContent>
          {filtered.length === 0 ? <EmptyState message="No devices found." /> : <DeviceTable devices={filtered} />}
        </CardContent>
      </Card>
    </div>
  );
}
