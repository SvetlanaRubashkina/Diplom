select c.login, count(o."courierId") from "Couriers" as c inner join "Orders" as o on c.id=o."courierId" where o."inDelivery"='true' group by c.login;