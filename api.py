from flask import Flask,request,jsonify
from datetime import datetime
api=Flask(__name__)

@api.route('/')
def apiCall():
    d={'status':'running','server':'localHost'}
    return jsonify(d)

def getTax(mrp,comod):
    if comod=='Medicine' or comod=='Food':
        tax=(mrp*5)/100
        return tax

    elif comod=='Music':
        tax=(mrp*3)/100
        return tax

    elif comod=='Clothes':
        if mrp<=1000:
            tax=(mrp*5)/100
        else:
            tax = (mrp * 12) / 100
        return tax

    elif comod=='Imported':
        tax=(mrp*18)/100
        return tax

    else:
        return 0


@api.route('/post',methods=['POST'])
def getItems():
    cart = request.get_json(force=True)
    qty=len(cart)
    bill={'Date & Time':datetime.now(),'Category':[],'Total':0,'Discount':0}
    if qty>0:
        try:
            for i in range(qty):
                bill['Date & Time'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

                tax = getTax(cart[i]['price'] * cart[i]['quantity'], cart[i]['itemCategory'])

                itemDetail = {'Item': cart[i]['item'], 'Price': cart[i]['price'] * cart[i]['quantity'], 'Tax': tax}

                cate = {cart[i]['itemCategory']: itemDetail}

                bill['Category'].append(cate)
                price=float((cart[i]['price'] * cart[i]['quantity'])+tax)
                bill['Total'] += price

            if bill['Total'] > 2000:
                bill['Discount'] = ((bill['Total'] * 5) / 100)
                bill['Total'] -= bill['Discount']
            return jsonify(bill)

        except Exception as error:
            return error







if __name__=="__main__":
    api.run(debug=True)