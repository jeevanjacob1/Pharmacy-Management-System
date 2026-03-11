from sqlalchemy import func

def get_total_revenue(db, Sale):
    total = db.session.query(func.sum(Sale.total_price)).scalar()
    if total is None:
        return 0.0
    return round(total, 2)
def get_most_sold_medicine(db, Sale, Medicine):
    sales = Sale.query.all()
    count_dict = {}
    for sale in sales:
        if sale.medicine_id in count_dict:
            count_dict[sale.medicine_id] += sale.quantity
        else:
            count_dict[sale.medicine_id] = sale.quantity
    if not count_dict:
        return "Nothing sold yet"
    best_id = max(count_dict, key=count_dict.get)
    best_qty = count_dict[best_id]

    med = Medicine.query.get(best_id)
    return f"{med.name} ({best_qty} sold)"

def get_stock_analysis(db, Medicine):
    medicines = Medicine.query.all()
    
    total_stock = 0
    low_stock = []
    
    for med in medicines:
        total_stock += med.quantity
        if med.quantity < 15:
            low_stock.append({"name": med.name, "stock": med.quantity})
    return {
        "total_items": total_stock,
        "low_stock_list": low_stock
    }
def get_monthly_sales_report(db, Sale):
    # Groups sales by month
    sales = Sale.query.all()
    monthly_report = {}
    for sale in sales:
        month = str(sale.date)[0:7] 
        if month in monthly_report:
            monthly_report[month] += sale.total_price
        else:
            monthly_report[month] = sale.total_price  
    return monthly_report
